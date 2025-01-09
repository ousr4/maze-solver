import random
import time

from geometry import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        nums_cols,
        cell_size_x,
        cell_size_y,
        windows=None,
        seed=None,
    ) -> None:
        if seed:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = nums_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._windows = windows
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_wall_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [
            [Cell(self._windows) for _ in range(self.num_cols)]
            for _ in range(self.num_rows)
        ]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._windows is None:
            return
        cell_x1 = self.cell_size_x * i + self.x1
        cell_y1 = self.cell_size_y * j + self.y1
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y
        if self._cells:
            self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
            self._animate()

    def _break_entrance_and_exit(self):
        # Create entrance
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        # Create exit
        self._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

    def _break_wall_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check left neighbour
            if i - 1 >= 0 and self._cells[i - 1][j].visited == False:
                to_visit.append((i - 1, j))
            # Chek top neighbour
            if j - 1 >= 0 and self._cells[i][j - 1].visited == False:
                to_visit.append((i, j - 1))
            # Check right neighbour
            if i + 1 < len(self._cells) and self._cells[i + 1][j].visited == False:
                to_visit.append((i + 1, j))
            # Check bottom neighbour
            if j + 1 < len(self._cells[0]) and self._cells[i][j + 1].visited == False:
                to_visit.append((i, j + 1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction_x, direction_y = to_visit[random.randrange(0, len(to_visit))]
            # Visit left neighbour
            if direction_x == i - 1 and direction_y == j:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_rigth_wall = False
            # Visit top neighbour
            if direction_x == i and direction_y == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # Visit right neighbour
            if direction_x == i + 1 and direction_y == j:
                self._cells[i][j].has_rigth_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # Visit bottom neighbour
            if direction_x == i and direction_y == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            self._break_wall_r(direction_x, direction_y)

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        # Check left neighbour
        if (
            i - 1 >= 0
            and self._cells[i - 1][j].visited == False
            and self._cells[i][j].has_left_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        # Chek top neighbour
        if (
            j - 1 >= 0
            and self._cells[i][j - 1].visited == False
            and self._cells[i][j].has_top_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        # Check right neighbour
        if (
            i + 1 < len(self._cells)
            and self._cells[i + 1][j].visited == False
            and self._cells[i][j].has_rigth_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        # Check bottom neighbour
        if (
            j + 1 < len(self._cells[0])
            and self._cells[i][j + 1].visited == False
            and self._cells[i][j].has_bottom_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        return False

    def _animate(self):
        if self._windows is None:
            return
        self._windows.redraw()
        time.sleep(0.01)

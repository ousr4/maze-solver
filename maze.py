from geometry import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, nums_cols, cell_size_x, cell_size_y, windows=None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = nums_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._windows = windows
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = [[Cell(self._windows) for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._windows is None:
            return
        cell_x1 = self.cell_size_x * i + self.x1
        cell_y1 = self.cell_size_y * j + self. y1
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y
        if self._cells:
            self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
            self._animate()

    def _break_entrance_and_exit(self):
        # Create entrance
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        #Create exit
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self._draw_cell(self.num_rows-1, self.num_cols-1)

    def _animate(self):
        if self._windows is None:
            return
        self._windows.redraw()
        time.sleep(0.05)

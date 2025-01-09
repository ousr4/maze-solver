from tkinter import BOTH, Canvas, Tk

from geometry import *
from maze import Maze


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(width=width, height=height)
        self.__canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)


def main():
    width = 800
    height = 600
    win = Window(width, height)
    border_size = 10
    num_cells = 20
    space_x = width - 2 * border_size
    space_y = height - 2 * border_size
    cell_size_x = space_x / num_cells
    cell_size_y = space_y / num_cells

    maze = Maze(
        border_size, border_size, num_cells, num_cells, cell_size_x, cell_size_y, win
    )
    if maze.solve():
        print("Maze solved succesfully")
    else:
        print("Failed to solve maze")
    win.wait_for_close()


if __name__ == "__main__":
    main()

from tkinter import BOTH, Canvas, Tk

from geometry import *


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
    win = Window(800, 600)
    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(10, 10, 60, 60)

    cell2 = Cell(win)
    cell2.has_rigth_wall = False
    cell2.draw(100, 100, 150, 150)

    cell.draw_move(cell2)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(225, 225, 275, 275)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(300, 300, 350, 350)
    win.wait_for_close()


if __name__ == "__main__":
    main()

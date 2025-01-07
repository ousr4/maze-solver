from tkinter import BOTH, Canvas, Tk

from geometry import *


class Window:
    def __init__(self, widht, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas()
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
    win.draw_line(Line(Point(50, 50), Point(200, 200)), "Black")
    win.wait_for_close()


if __name__ == "__main__":
    main()

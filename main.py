from tkinter import BOTH, Canvas, Tk


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


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()

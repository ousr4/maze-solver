from tkinter import Canvas


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point: ({self.x, self.y})"


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, window=None) -> None:
        self.has_left_wall = True
        self.has_rigth_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window

    def draw(self, x1, y1, x2, y2) -> None:
        if self._window is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        wall_color = "Black" if self.has_left_wall else "#d9d9d9"
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        self._window.draw_line(left_wall, wall_color)

        wall_color = "Black" if self.has_rigth_wall else "#d9d9d9"
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        self._window.draw_line(right_wall, wall_color)

        wall_color = "Black" if self.has_top_wall else "#d9d9d9"
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        self._window.draw_line(top_wall, wall_color)

        wall_color = "Black" if self.has_bottom_wall else "#d9d9d9"
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        self._window.draw_line(bottom_wall, wall_color)

    def draw_move(self, to_cell, undo=False):
        fill_color = "Red"
        if undo:
            fill_color = "Gray"
        if (
            self._x1
            and self._x2
            and self._y1
            and self._y2
            and to_cell._x1
            and to_cell._x2
            and to_cell._y1
            and to_cell._y2
        ):
            start = Point(
                self._x1 + (self._x2 - self._x1) / 2,
                self._y1 + (self._y2 - self._y1) / 2,
            )
            end = Point(
                to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2,
                to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2,
            )
            print(start)
            print(end)
            line = Line(start, end)
            self._window.draw_line(line, fill_color)

    def __repr__(self) -> str:
        return f"Cell: ({self._x1}, {self._y1}) ({self._x2}, {self._y2})"

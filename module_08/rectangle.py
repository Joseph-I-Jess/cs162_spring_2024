"""Describe a rectangle shape object."""
import tkinter as tk # for the Canvas class

import shape # for the Shape class

class Rectangle(shape.Shape):
    """Represent a rectangle shape whose outer edges are determined by (x0, y0) and (x1, y1) as the outer most points of the shape."""
    def __init__(self, x0=0, y0=0, x1=0, y1=0, fill="yellow", outline="purple", canvas=None):
        super().__init__(x0, y0, x1, y1, fill, outline)
        self.id: int | None = None # what is the id of the graphic item that my data is attached to
        self.canvas: tk.Canvas | None = canvas # what canvas am I being drawn on

    def get_area(self):
        """Calculate and return area of rectangle."""
        width = self.x1 - self.x0
        height = self.y1 - self.y0

        area = width * height

        return area
    
    def set_canvas(self, new_canvas: tk.Canvas):
        self.canvas = new_canvas

    def draw_yo_self(self):
        """Draw yourself on a given canvas."""
        if self.canvas is not None:
            self.id = self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.fill, outline=self.outline)
        else:
            print("Canvas object has not been set yet!")

    def move_right(self):
        """Move this object right 1 pixel."""
        self.x0 += 1
        self.x1 += 1

        if self.canvas is not None and self.id is not None:
            print(f"self.id: {self.id}")
            self.canvas.coords(self.id, (self.x0, self.y0, self.x1, self.y1))
        else:
            print("Canvas object has not been set yet or object has not been created with an id yet!")

        print(f"coordinates: ({self.x0},{self.y0})-({self.x1},{self.y1})")


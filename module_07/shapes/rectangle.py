"""Describe a rectangle shape object."""
import tkinter as tk

import shape

class Rectangle(shape.Shape):
    def __init__(self, x0=0, y0=0, x1=0, y1=0, fill="red", outline="blue"):
        super().__init__(x0, y0, x1, y1, fill, outline)

    def get_area(self):
        """Calculate and return area of rectangle."""
        width = self.x1 - self.x0
        height = self.y1 - self.y0

        area = width * height

        return area
    
    def draw_yo_self(self, canvas: tk.Canvas):
        """Draw yourself on a given canvas."""
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.fill, outline=self.outline)

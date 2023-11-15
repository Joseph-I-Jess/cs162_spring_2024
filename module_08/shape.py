"""Create a generic shape class."""

import tkinter as tk # for the Canvas class

class ShapeError(Exception):
    """Basic exception for all shape errors."""
    def __init__(self, message="A ShapeError occurred."):
        super().__init__()
        self.message: str = message

class ShapeInitializationError(ShapeError):
    """Exception for a shape not yet fully initialized."""
    def __init__(self, message="A ShapeInitilizationError occurred, did you remember to assign a value to canvas and id?"):
        super().__init__(message)

class Shape:
    """Represents a generic shape."""
    def __init__(self, x0=0, y0=0, x1=0, y1=0, fill="red", outline="blue", canvas=None):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.fill = fill
        self.outline = outline
        self.id: int | None = None # what is the id of the graphic item that my data is attached to
        self.canvas: tk.Canvas | None = canvas # what canvas am I being drawn on
        # self.canvas_shape: str | None = None

    def set_canvas(self, new_canvas: tk.Canvas):
        self.canvas = new_canvas

    def draw_yo_self(self):
        """Draw yourself on a given canvas.
        
            Raises a ShapeInitializationError if self.canvas is None"""
        if self.canvas is not None:
            self.id = self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.fill, outline=self.outline)
        else:
            raise ShapeInitializationError("Canvas object has not been set yet on this shape!")

    def move_right(self):
        """Move this object right 1 pixel.
        
            Raises a ShapeInitializationError if self.canvas is None or self.id is None"""
        self.x0 += 1
        self.x1 += 1

        if self.canvas is not None and self.id is not None:
            print(f"self.id: {self.id}")
            self.canvas.coords(self.id, (self.x0, self.y0, self.x1, self.y1))
        else:
            raise ShapeInitializationError("Canvas object has not been set yet or object has not been created with an id yet!")

        print(f"coordinates: ({self.x0},{self.y0})-({self.x1},{self.y1})")

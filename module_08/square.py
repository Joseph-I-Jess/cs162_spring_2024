"""Describe a square object."""

import rectangle

class Square(rectangle.Rectangle):
    """Stuff..."""

    def __init__(self, x0, y0, size, fill="orange", outline="brown", canvas=None):
        super().__init__(x0, y0, x0 + size, y0 + size, fill, outline, canvas)

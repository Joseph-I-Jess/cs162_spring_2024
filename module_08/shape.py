"""Create a generic shape class."""

class Shape:
    """Represents a generic shape."""
    def __init__(self, x0=0, y0=0, x1=0, y1=0, fill="red", outline="blue"):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.fill = fill
        self.outline = outline

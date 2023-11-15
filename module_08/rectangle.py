"""Describe a rectangle shape object."""
import shape # for the Shape class

class AreaError(Exception):
    def __init__(self, message="A AreaError has occurred.", area=0):
        super().__init__()
        self.area = area

class Rectangle(shape.Shape):
    """Represent a rectangle shape whose outer edges are determined by (x0, y0) and (x1, y1) as the outer most points of the shape."""

    def get_area(self):
        """Calculate and return area of rectangle."""
        width = self.x1 - self.x0
        height = self.y1 - self.y0

        # area = abs(width * height)
        area = width * height
        if area < 0:
            raise AreaError(area=area)

        return area

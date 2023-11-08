
import tkinter as tk

import shape
import rectangle
import square

def main():

    # setup GUI
    root = tk.Tk()

    canvas = tk.Canvas(root, width=400, height=300)
    canvas.grid(row = 0, column=0)

    # create shape respresentation objects
    shape_0 = shape.Shape(10, 10, 20, 40)
    rectangle_0 = rectangle.Rectangle(10, 50, 20, 60)
    square_0 = square.Square(10, 70, 20)
    square_1 = square.Square(10, 100, 30)
    square_1.fill = "purple"

    # represent shapes on canvas
    canvas.create_line(shape_0.x0, shape_0.y0, shape_0.x1, shape_0.y1, fill=shape_0.fill)
    # canvas.create_rectangle(rectangle_0.x0, rectangle_0.y0, rectangle_0.x1, rectangle_0.y1, fill=rectangle_0.fill, outline=rectangle_0.outline)
    rectangle_0.draw_yo_self(canvas)
    # canvas.create_rectangle(square_0.x0, square_0.y0, square_0.x1, square_0.y1, fill=square_0.fill, outline=square_0.outline)
    square_0.draw_yo_self(canvas)
    square_1.draw_yo_self(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
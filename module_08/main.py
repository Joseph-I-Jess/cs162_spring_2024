
import tkinter as tk

import shape
import rectangle
import square

# I do not like globals >:(
selected_rectangle: rectangle.Rectangle | None = None
rectangles: list[rectangle.Rectangle] = []

def random_color(canvas: tk.Canvas, id: int):
    """Set fill color and outline of item with id in canvas to a random color."""
    global rectangles
    global selected_rectangle

    color = "green"
    canvas.itemconfig(id, fill=color)
    for current_rectangle in rectangles:
        if current_rectangle.id == id:
            selected_rectangle = current_rectangle

def main():

    global selected_rectangle

    # setup GUI
    root = tk.Tk()

    canvas = tk.Canvas(root, width=400, height=300)
    canvas.grid(row = 0, column=0)

    # THE FOLLOWING CODE SHOULD HAVE INPUT VALIDATION!!!
    random_color_button = tk.Button(root, text="Click to select item and highlight with color", command=lambda: random_color(canvas, int(id_entry.get())))
    random_color_button.grid(row=1, column=0)

    move_right_button = tk.Button(root, text="move selected item right", command=lambda: selected_rectangle.move_right())
    move_right_button.grid(row=2, column=1)

    id_entry = tk.Entry(root, width=10)
    id_entry.grid(row=1, column=1)

    # create shape respresentation objects
    shape_0 = shape.Shape(10, 10, 20, 40)
    rectangle_0 = rectangle.Rectangle(10, 50, 40, 60, canvas=canvas) # canvas=canvas, first canvas is rectangle paramater while second canvas is the canvas object in the local scope (defined up above in this current script)
    square_0 = square.Square(10, 70, 20)
    square_0.set_canvas(canvas)
    square_1 = square.Square(10, 100, 30)
    square_1.set_canvas(canvas)
    square_1.fill = "purple"

    rectangles.append(rectangle_0)
    rectangles.append(square_0)
    rectangles.append(square_1)

    # represent shapes on canvas
    canvas.create_line(shape_0.x0, shape_0.y0, shape_0.x1, shape_0.y1, fill=shape_0.fill)
    # canvas.create_rectangle(rectangle_0.x0, rectangle_0.y0, rectangle_0.x1, rectangle_0.y1, fill=rectangle_0.fill, outline=rectangle_0.outline)
    rectangle_0.draw_yo_self()
    # canvas.create_rectangle(square_0.x0, square_0.y0, square_0.x1, square_0.y1, fill=square_0.fill, outline=square_0.outline)
    square_0.draw_yo_self()
    square_1.draw_yo_self()

    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk

import shape
import rectangle
import square

# I do not like globals >:(
selected_shape: shape.Shape | None = None
shapes: list[shape.Shape] = []

def random_color(canvas: tk.Canvas, id: int):
    """Set fill color and outline of item with id in canvas to a random color."""
    global shapes
    global selected_shape

    color = "green"
    canvas.itemconfig(id, fill=color)
    for current_shape in shapes:
        if current_shape.id == id:
            selected_shape = current_shape

def main():

    global selected_shape

    # setup GUI
    root = tk.Tk()

    my_canvas = tk.Canvas(root, width=400, height=300)
    my_canvas.grid(row = 0, column=0)

    # THE FOLLOWING CODE SHOULD HAVE INPUT VALIDATION!!!
    random_color_button = tk.Button(root, text="Click to select item and highlight with color", command=lambda: random_color(my_canvas, int(id_entry.get())))
    random_color_button.grid(row=1, column=0)

    # should we move the selected_rectangle.move_right() into a helper function that can do a None check or make a long conditional in-line statement?
    move_right_button = tk.Button(root, text="move selected item right", command=lambda: selected_shape.move_right())
    move_right_button.grid(row=2, column=1)

    id_entry = tk.Entry(root, width=10)
    id_entry.grid(row=1, column=1)

    # create shape respresentation objects
    shape_0 = shape.Shape(10, 10, 20, 40, canvas=my_canvas)
    rectangle_0 = rectangle.Rectangle(10, 50, 40, 60, canvas=my_canvas) # canvas=canvas, first canvas is rectangle paramater while second canvas is the canvas object in the local scope (defined up above in this current script)
    # square_0 = square.Square(10, 70, 20) # will throw a ShapeInitilizationError
    square_0 = square.Square(10, 70, 20, canvas=my_canvas)
    square_1 = square.Square(10, 100, 30, fill="purple", canvas=my_canvas)

    shapes.append(shape_0)
    shapes.append(rectangle_0)
    shapes.append(square_0)
    shapes.append(square_1)

    # represent shapes on canvas
    # hard coded, magic avlue, deciding that the default shape is a line... this canvas item does not have a move_right method, because it is not a "shape" object!
    my_canvas.create_line(shape_0.x0, shape_0.y0, shape_0.x1, shape_0.y1, fill=shape_0.fill)
    # attempt to draw the shapes
    for current_shape in shapes:
        try:
            current_shape.draw_yo_self()
        except shape.ShapeInitializationError as sie:
            print(f"A ShapeInitilizationError has occurred: {sie.message}")
    # shape_0.draw_yo_self() # should raise exception
    # # canvas.create_rectangle(rectangle_0.x0, rectangle_0.y0, rectangle_0.x1, rectangle_0.y1, fill=rectangle_0.fill, outline=rectangle_0.outline)
    # rectangle_0.draw_yo_self()
    # # canvas.create_rectangle(square_0.x0, square_0.y0, square_0.x1, square_0.y1, fill=square_0.fill, outline=square_0.outline)
    # square_0.draw_yo_self()
    # square_1.draw_yo_self()

    # try to create a negative area rectangle
    rectangle_negative_area = rectangle.Rectangle(20, 130, -20, 120, "black", "blue", my_canvas)
    shapes.append(rectangle_negative_area)
    rectangle_negative_area.draw_yo_self()
    # what are the coordinates in my_canvas for the negative area rectangle?
    # does Canvas order our coords from lesser to greater for each axis...
    if rectangle_negative_area.id is not None:
        coords = my_canvas.coords(rectangle_negative_area.id)
        print(f"rectangle_negative_area has coords in canvas of: {coords}")
    else:
        print(f"rectangle_negative_area.id is None, try setting id or drawing the shape first.")
    try:
        area = rectangle_negative_area.get_area()
    except rectangle.AreaError as ae:
        area = abs(ae.area)
    print(f"rectangle_negative_area.get_area(): {area}")

    root.mainloop()

if __name__ == "__main__":
    main()
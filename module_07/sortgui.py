"""Contain definition for a GUI that demonstrates sorting capabilities."""

import time # for sleep
import tkinter as tk # lots of GUI widgets
# from tkinter import messagebox # for showinfo message box, no longer used

import rectangle

class SortGui:
    """Create a GUI that can be manipulated to show sorting algorithms."""

    def __init__(self, initial_values: list[int]) -> None:
        """Create a canvas of rectangles that can later be highlighted and un-highlighted as needed later."""
        #########################################################################
        # data for this GUI
        #########################################################################
        # The list of values for our initially drawn rectangles.
        self.values = initial_values
        # rectangle objects
        self.rectangles: list[rectangle.Rectangle] = []
        # A list of indices that are related to the canvas rectangles created later in this code.
        self.rectangle_indices = []
        self.sleep_delay = 0.5

        # Indicates the "status" of the rectangles, for example, green is a matched value, yellow is a values not yet checked, and red is a checked value that is a non-match.
        self.unchecked_value_highlight = "white"
        self.candidate_value_highlight = "yellow"
        self.sorted_value_highlight = "green"

        #########################################################################
        # create GUI
        #########################################################################

        # create toplevel
        self.root = tk.Tk()

        # create canvas to display results
        self.canvas = tk.Canvas(self.root, height=120, width=400, bg="lightgray")
        self.canvas.grid(row=0, column=0)

        # create entry for user input, to be used for seraching algorithms
        self.sleep_duration_input = tk.Entry(self.root)
        self.sleep_duration_input.bind("<Return>", self.update_sleep)
        self.sleep_duration_input.grid(row=1, column=0)

        # create button to later start the search process
        self.start_sort_button = tk.Button(self.root, text="start sort", command=self.sort)
        self.start_sort_button.grid(row=1, column=1)

        # create button to later draw rectangles on the canvas
        self.populate_button = tk.Button(self.root, text="draw rectangles", command=self.populate_canvas)
        self.populate_button.grid(row=2, column=1)

        # initialize rectangles on GUI
        self.rect_width = 20

        self.x_offset = 10 # buffer between left edge of canvas and first rectangle
        self.x_step = self.rect_width + 5 # horizontal spacing between rectangles

        self.y_offset = 10 # buffer between top edge of canvas and rectangles
        self.value_multiplier = 5 # multiplier of value to determine rectangle height

        # Draw some rectangles based on the initial_values list and append the index returned to the rectangle_indices.
        for index,value in enumerate(initial_values):
            x0 = self.x_offset + self.x_step * index
            y0 = self.y_offset # a bit useless
            x1 = x0 + self.rect_width
            y1 = y0 + value * self.value_multiplier
            new_rectangle = rectangle.Rectangle(x0, y0, x1, y1, self.unchecked_value_highlight, "red")
            self.rectangles.append(new_rectangle)
            
            # self.rectangle_indices.append(self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.unchecked_value_highlight))
            # new_rectangle.canvas_id = self.canvas.create_rectangle(new_rectangle.x0, new_rectangle.y0, new_rectangle.x1, new_rectangle.y1, fill=new_rectangle.fill, outline=new_rectangle.outline)
            # self.rectangle_indices.append(new_rectangle.canvas_id)

    def populate_canvas(self):
        """Actually draw rectangles and fill in rectangle_indices list and disable the button."""
        self.populate_button["state"] = "disabled"

        for rect in self.rectangles:
            # rect.canvas_id = self.canvas.create_rectangle(rect.x0, rect.y0, rect.x1, rect.y1, fill=rect.fill, outline=rect.outline)
            rect.canvas_id = rect.draw_yo_self(self.canvas)
            self.rectangle_indices.append(rect.canvas_id)

        # debug to test swap_height_of_indices method in simple context
        # self.test_swap_button = tk.Button(self.root, text="swap height of rectangle_indices[0] and rectangle_indices[1]", command=lambda: self.swap_height_of_indices(self.rectangle_indices[0], self.rectangle_indices[1]))
        # self.test_swap_button.grid(row=2, column=1)

        # debug to test sort_step method in simple context
        # self.test_sort_step_button = tk.Button(self.root, text="test sort step on position 0", command=lambda: print(f"self.sort_step(0): {self.sort_step(0)}"))
        # self.test_sort_step_button.grid(row=2, column=1)

    def mainloop(self):
        """Pass mainloop call on to this GUI's Toplevel object."""
        self.root.mainloop()

    def update_sleep(self, event):
        try:
            self.sleep_delay = float(self.sleep_duration_input.get())
        except ValueError:
            print(f"Value error occurred, try a floating point value in the enrty box instead!")
            raise ValueError

    def sort(self):
        """Method to sort GUI rectangles."""
        # initialize rectangle colors to be unchecked
        for id in self.rectangle_indices:
            self.canvas.itemconfig(id, fill=self.unchecked_value_highlight)
        
        # run a loop over all indices, performing a sort_step on each index.
        # source and destination are canvas ids
        for source in self.rectangle_indices:
            # highlight current position
            self.canvas.itemconfig(source, fill=self.candidate_value_highlight)
            self.root.update()
            # pause to see highlight
            time.sleep(self.sleep_delay)
            # find swap partner
            destination = self.sort_step(source)
            # highlight swap partner
            self.canvas.itemconfig(destination, fill=self.candidate_value_highlight)
            self.root.update()
            # sleep to see highlited rectangles
            time.sleep(self.sleep_delay)
            # perform swap
            self.swap_height_of_indices(source, destination)
            self.root.update()
            # sleep to see swapped heights
            time.sleep(self.sleep_delay)
            # unhighlight candidate and highlight final swapped value as matched
            self.canvas.itemconfig(destination, fill=self.unchecked_value_highlight)
            self.canvas.itemconfig(source, fill=self.sorted_value_highlight)
            self.root.update()
            # sleep to show final stage of sort step being fifnished
            time.sleep(self.sleep_delay)

        


    def sort_step(self, current_index):
        """Helper method that perform one step in a selection sort algorithm at the given current_index (a canvas id) and return the index of the smallest height rectangle in the canvas."""
        # find index of rectangle with smallest height in the list remaining to be sorted
        # first index in list to be sorted has the smallest height so far
        smallest_index_so_far = current_index
        smallest_index_coords = self.canvas.coords(smallest_index_so_far)
        smallest_height_so_far = smallest_index_coords[3] - smallest_index_coords[1] # y1 - y0

        # then walk through remaining list and see if any later rectangles have a smaller height
        for candidate_index in self.rectangle_indices[current_index:]:
            # fetch coords to do calculations
            candidate_coords = self.canvas.coords(candidate_index)
            # calculate height
            candidate_height = candidate_coords[3] - candidate_coords[1]
            # check if candidate height is smaller than smallest height so far
            if candidate_height < smallest_height_so_far:
                # then keep track of candidate instead of previous smallest seen so far
                smallest_index_so_far = candidate_index
                smallest_height_so_far = candidate_height

        # return index
        return smallest_index_so_far

    def swap_height_of_indices(self, source_id, destination_id):
        """Swap y1 of rectangle with source as its canvas index with the y1 of rectangle with destination as its canvas index."""
        # may need to check that y1 is larger than y0 value...!
        source_coords = self.canvas.coords(source_id)
        destination_coords = self.canvas.coords(destination_id)

        # debug
        # print(f"source_coords: {source_coords}")
        # print(f"destination_coords: {destination_coords}")

        # swap coords of (source y1, destination y1) to be (destination y1, source y1)
        (source_coords[3], destination_coords[3]) = (destination_coords[3], source_coords[3])

        # set coords back into canvas items
        self.canvas.coords(source_id, source_coords)
        self.canvas.coords(destination_id, destination_coords)

"""Contain definition for a GUI that demonstrates searching capabilities."""

import random
import tkinter as tk
from tkinter import messagebox

class SearchGui:
    """Create a GUI that can be manipulated to show searching algorithms."""

    def __init__(self, initial_values: list[int]) -> None:
        """Create a canvas of rectangles that can later be highlighted and un-highlighted as needed later."""
        #########################################################################
        # data for this GUI
        #########################################################################
        # The list of values for our initially drawn rectangles.
        self.values = initial_values
        # A list of indices that are related to the canvas rectangles created later in this code.
        self.rectangle_indices = []

        # Indicates the "status" of the rectangles, for example, green is a matched value, yellow is a values not yet checked, and red is a checked value that is a non-match.
        self.matched_value_highlight = "green"
        self.unmatched_value_highlight = "yellow"

        #########################################################################
        # create GUI
        #########################################################################

        # create toplevel
        self.root = tk.Tk()

        # create canvas to display results
        self.canvas = tk.Canvas(self.root, height=600, width=800, bg="lightgray")
        self.canvas.grid(row=0, column=0)

        # create entry for user input, to be used for seraching algorithms
        self.search_input = tk.Entry(self.root)
        self.search_input.grid(row=1, column=0)

        # create button to later start the search process
        self.start_search_button = tk.Button(self.root, text="start search", command=self.search)
        self.start_search_button.grid(row=1, column=1)

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
            
            self.rectangle_indices.append(self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.unmatched_value_highlight))

    def mainloop(self):
        """Pass mainloop call on to this GUI's Toplevel object."""
        self.root.mainloop()

    def highlight_rectangle(self, index, color):
        """Highlight item with index in canvas with color after a delay."""
        self.canvas.itemconfig(index, fill=color)
    
    def search(self):
        """Find all instances of rectangles.
        
            Find all instances of rectangles with a height dteermined by a user-selected
              value in this object's canvas and highlight them.

            parameters: none
            return: none
        """
        result = [] # 

        # grab search candidate
        candidate = self.search_input.get()
        try:
            candidate = int(candidate)
        except ValueError:
            messagebox.showinfo(title="Alert!?!", message=f"{candidate} is an invalid value, try again")
            print(f"{candidate} is an invalid value, try again")

        # debug
        #print(f"candidate: {candidate}")

        # walk through list, highlight as we go
        for index in self.rectangle_indices:
            coords = self.canvas.coords(index)
            y0 = coords[1]
            y1 = coords[3]
            height = y1 - y0

            # debug
            print(f"height at index {index}: {height}")

            # Highlight this rectangle with either a matched color or a non-match color.
            delay = 100 * index
            if height == candidate * self.value_multiplier:
                # self.canvas.itemconfig(index, fill=self.matched_value_highlight)
                # does not quite work # self.root.after(100 * index, self.highlight_rectangle(index, self.matched_value_highlight))
                self.canvas.itemconfig(index, fill=self.matched_value_highlight)
                self.root.after(delay, self.root.update())
            else:
                # self.canvas.itemconfig(index, fill=self.unmatched_value_highlight)
                # does not quite work # self.root.after(100 * index, self.highlight_rectangle(index, self.unmatched_value_highlight))
                self.canvas.itemconfig(index, fill=self.unmatched_value_highlight)
                self.root.after(delay, self.root.update())



# script stuff

# We could start our testing with some known values.
# sg = SearchGui([1, 0, 3, 5, 9, 2, 7, 5, 2, 3, 6])

# We could then use random values to test a larger variety of cases.
rando_list = []
for i in range(10):
    rando_list.append(random.randint(5, 5))
sg = SearchGui(rando_list)
sg.mainloop()

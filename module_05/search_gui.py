import random
import tkinter as tk
from tkinter import messagebox

class SearchGui:
    """Create a GUI that can be manipulated to show searching algorithms."""

    def __init__(self, initial_values: list[int]) -> None:
        """Create a canvas of rectangles that can later be highlighted and un-highlighted as needed later."""
        
        # data for this GUI
        self.values = initial_values
        self.rectangle_indices = []

        self.matched_value_highlight = "green"
        self.unmatched_value_highlight = "yellow"

        # create GUI

        # create toplevel
        self.root = tk.Tk()

        # create canvas to display results
        self.canvas = tk.Canvas(self.root, height=600, width=800, bg="lightgray")
        self.canvas.grid(row=0, column=0)

        # create entry for user input
        self.search_input = tk.Entry(self.root)
        self.search_input.grid(row=1, column=0)

        # create button to kick off search process
        self.start_search_button = tk.Button(self.root, text="start search", command=self.search)
        self.start_search_button.grid(row=1, column=1)

        # initialize rectangles on GUI
        self.rect_width = 20

        self.x_offset = 10
        self.x_step = self.rect_width + 5

        self.y_offset = 10
        self.y_step = 5

        for index,value in enumerate(initial_values):
            x0 = self.x_offset + self.x_step * index
            y0 = self.y_offset # a bit useless
            x1 = x0 + self.rect_width
            y1 = y0 + value * self.y_step
            
            self.rectangle_indices.append(self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.unmatched_value_highlight))

    def mainloop(self):
        self.root.mainloop()

    def search(self):
        """Find all instances of a value in this object's internal list and highlight them."""
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
            #print(f"height at index {index}: {height}")

            if height == candidate * self.y_step:
                self.canvas.itemconfig(index, fill=self.matched_value_highlight)
            else:
                self.canvas.itemconfig(index, fill=self.unmatched_value_highlight)

# script stuff
# sg = SearchGui([1, 0, 3, 5, 9, 2, 7, 5, 2, 3, 6])
rando_list = []
for i in range(10):
    rando_list.append(random.randint(1, 20)) 
sg = SearchGui(rando_list)
sg.mainloop()

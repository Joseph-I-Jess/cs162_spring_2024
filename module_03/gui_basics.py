"""Experiment with some basic GUI widgets and behaviors."""
# definition stuff...
import tkinter as tk

class GuiBasics:
    """Demo basic GUIs, now with class!"""

    def __init__(self):
        """Initilize this GUI.
        
            Creates several widgets, aligns them to the specified layout in
            document "blah blah blah".pdf for company XYZ...

            Takes no parameters, returns no special values.
        """

        # root of GUI
        self.root = tk.Tk()
        self.root.minsize(800, 600)

        # label
        self.label = tk.Label(self.root, text="this is a label")
        self.label.grid(column=0, row=0)

        # buttons
        self.button = tk.Button(self.root, text="Click me!", command=self.button_clicked)
        self.button.grid(column=0, row=1)

        self.button_2 = tk.Button(self.root, text="Click me 2!", command=lambda: self.button_clicked(self.entry_stringvar.get()))
        self.button_2.grid(column=1, row=1)

        # entry (text box)
        self.entry_stringvar = tk.StringVar(self.root, "This is a stringvar!")
        # print(f"self.entry_stringvar immediately after creation: {self.entry_stringvar.get()}")
        self.entry = tk.Entry(self.root, textvariable=self.entry_stringvar, width=100)
        # insert also works!
        # entry.insert(0, "hello?01234567890123456789012345678901234567890123456789")
        self.entry.grid(column=1, row=2)

        # alter stringvar, watch what happens!
        # entry_stringvar = "hello" # don't do this to set the value of the stringvar's contents!
        # self.entry_stringvar.set("Update stringvar!")

    def button_clicked(self, new_text="no new text was entered"):
        # print("button clicked!")
        # user_input = entry_stringvar.get()
        # could alsu set the value of a stringvar associated with the label instead...
        self.label.config(text=new_text)

    def mainloop(self):
        """Start this GUI in a window."""
        self.root.mainloop()

# script stuff...
# if __name__ == "__main__":
#     print(f"__name__ in gui_basics.py: {__name__}")

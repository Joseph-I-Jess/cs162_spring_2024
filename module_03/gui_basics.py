"""Experiment with some basic GUI widgets and behaviors."""

import tkinter as tk

# root of GUI
root = tk.Tk()
root.minsize(800, 600)

# label
label = tk.Label(root, text="this is a label")
label.grid(column=0, row=0)

# buttons
def button_clicked(new_text="no new text was entered"):
    print("button clicked!")
    # user_input = entry_stringvar.get()
    # could alsu set the value of a stringvar associated with the label instead...
    label.config(text=new_text)

button = tk.Button(root, text="Click me!", command=button_clicked)
button.grid(column=0, row=1)

button_2 = tk.Button(root, text="Click me 2!", command=lambda: button_clicked(entry_stringvar.get()))
button_2.grid(column=1, row=1)

# entry (text box)
entry_stringvar = tk.StringVar(root, "This is a stringvar!")
entry = tk.Entry(root, textvariable=entry_stringvar, width=100)
# insert also works!
# entry.insert(0, "hello?01234567890123456789012345678901234567890123456789")
entry.grid(column=1, row=2)

# alter stringvar, watch what happens!
# entry_stringvar = "hello" # don't do this to set the value of the stringvar's contents!
entry_stringvar.set("Update stringvar!")

# start GUI window
root.mainloop()

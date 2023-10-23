"""Demo actual use of a GuiBasics object."""
# import and define stuff...
import gui_basics

def main():
    # create some GUIs

    gui_2 = gui_basics.GuiBasics()
    gui_2.root.withdraw()
    gui_2.update_label("hello (world again!?), this is gui_2!")
    
    # create the window that I want to hjave focus on last, so Windows has this window with focus
    gui = gui_basics.GuiBasics()

    # modify GUI objects to know about each other (optional)
    gui.register_partner_gui(gui_2)
    gui_2.register_partner_gui(gui)

    # start GUI
    gui.mainloop()
    # gui_2.mainloop()

    # if I get here, my gui mainloop has ended, so clean up other things
    # gui_2.root.destroy()
    print("Got to end of main!")

# run some script stuff...
print(f"__name__ in main.py: {__name__}")

if __name__ == "__main__":
    main()

"""Demo actual use of a GuiBasics object."""
# import and define stuff...
import gui_basics

def main():
    print("in main, just passing for now...")
    gui = gui_basics.GuiBasics()

    gui_2 = gui_basics.GuiBasics()
    gui_2.update_label("hello (world again!?), this is gui_2!")
    
    gui.register_partner_gui(gui_2)
    gui_2.register_partner_gui(gui)

    gui.mainloop()
    gui_2.mainloop()

# run some script stuff...
print(f"__name__ in main.py: {__name__}")

if __name__ == "__main__":
    main()

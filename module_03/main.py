"""Demo actual use of a GuiBasics object."""
# import and define stuff...
import gui_basics

def main():
    print("in main, just passing for now...")
    gui = gui_basics.GuiBasics()
    gui.mainloop()

# run some script stuff...
print(f"__name__ in main.py: {__name__}")

if __name__ == "__main__":
    main()

"""Demo use of GUI elements to simulate sorting."""
import random

import sortgui

def main():
    # create a sort GUI

    # We could start our testing with some known values.
    # sg = SearchGui([1, 0, 3, 5, 9, 2, 7, 5, 2, 3, 6])

    # We could then use random values to test a larger variety of cases.
    # rando_list = []
    # for i in range(10):
    #     rando_list.append(random.randint(1, 20))
    rando_list = [random.randint(1, 20) for num in range(0, 10)]
    print(f"rando_list: {rando_list}")
    sg = sortgui.SortGui(rando_list)
    sg.mainloop()

    print("Got to end of main!")

# run some script stuff...
print(f"__name__ in main.py: {__name__}")

if __name__ == "__main__":
    main()

"""Test the sortgui module."""

import pytest

import sortgui

def test_mainloop():
    initial_list = [10]
    sg = sortgui.SortGui(initial_list)

    expected_height = initial_list[0] * sg.value_multiplier

    actual_coords = sg.canvas.coords(1)
    actual_height = actual_coords[3] - actual_coords[1]

    sg.root.after(100, sg.root.quit)
    sg.mainloop()

    assert actual_height == expected_height

def test_default_sortgui():
    """Test that default SortGUI object has expected default values."""

    ###############################################################################################
    # setup default object to be tested
    initial_list = [10, 20, 30]
    sg = sortgui.SortGui(initial_list)
    ###############################################################################################




    ###############################################################################################
    # first object on canvas is canvas_id 1
    expected_canvas_id = 1
    actual_canvas_id = sg.rectangle_indices[0]

    assert actual_canvas_id == expected_canvas_id # because I know how our sortgui works, with a canvas, and how a tkinter Canvas object works, by creating a list of integer indices..
    ###############################################################################################



    ###############################################################################################
    # expected height
    expected_height = sg.value_multiplier * initial_list[0]

    # calculate actual height of first rectangle
    actual_coords = sg.canvas.coords(sg.rectangle_indices[0])
    actual_height = actual_coords[3] - actual_coords[1]

    # height of first canvas object should be value_multiplier * first item in initial_list
    assert actual_height == expected_height
    ###############################################################################################


def test_update_sleep():
    """Test that the update sleep method actually sets the sleep_delay."""

    # setup object to be tested
    initial_list = [10]
    sg = sortgui.SortGui(initial_list)

    # expected sleep delay value
    expected_sleep_delay = 1.1

    # update sleep delay
    sg.search_input.insert(0, expected_sleep_delay)
    sg.update_sleep(None)

    # get actual sleep delay
    actual_sleep_delay = sg.sleep_delay

    # test that actual sleep delay is as expected
    assert actual_sleep_delay == expected_sleep_delay

def test_update_sleep_exception():
    """Test that the update sleep method actually sets the sleep_delay."""

    # setup object to be tested
    initial_list = [10]
    sg = sortgui.SortGui(initial_list)

    # expected sleep delay value
    expected_sleep_delay = "cats"

    # update sleep delay
    sg.search_input.insert(0, expected_sleep_delay)
    with pytest.raises(ValueError):
        sg.update_sleep(None)

    # we pass if the exception happens

def test_swap_height_of_indices():
    """Test that swap height of indices works on known data."""

    # setup object to be tested
    initial_list = [10, 20]
    sg = sortgui.SortGui(initial_list)

    # grab height of rectangles initially
    initial_coords_1 = sg.canvas.coords(sg.rectangle_indices[0])
    initial_height_1 = initial_coords_1[3] - initial_coords_1[1]
    initial_coords_2 = sg.canvas.coords(sg.rectangle_indices[1])
    initial_height_2 = initial_coords_2[3] - initial_coords_2[1]

    # expected heights of rectangles
    expected_height_1 = initial_height_2
    expected_height_2 = initial_height_1

    # swap ractangle heights
    sg.swap_height_of_indices(sg.rectangle_indices[0], sg.rectangle_indices[1])

    # actual heights after swap
    actual_coords_1 = sg.canvas.coords(sg.rectangle_indices[0])
    actual_height_1 = actual_coords_1[3] - actual_coords_1[1]
    actual_coords_2 = sg.canvas.coords(sg.rectangle_indices[1])
    actual_height_2 = actual_coords_2[3] - actual_coords_2[1]

    # assert swapped actual values matches expected values
    assert actual_height_1 == expected_height_1
    assert actual_height_2 == expected_height_2

def test_sort_step():
    """Test that sort step returns index of canvas id with smallest height"""
    # setup object to be tested
    smallest_value = 10
    initial_list = [smallest_value, 20]
    sg = sortgui.SortGui(initial_list)

    # expected canvas id with smallest height in pixels
    expected_smallest_index = 1
    expected_smallest_height = smallest_value * sg.value_multiplier

    # fetch sort step data (should be canvas id of smallest height rectangle (in pixels))
    actual_smallest_index = sg.sort_step(1)
    actual_smallest_height = (sg.canvas.coords(actual_smallest_index)[3] - sg.canvas.coords(actual_smallest_index)[1])

    # check actual versus expected
    assert actual_smallest_index == expected_smallest_index
    assert actual_smallest_height == expected_smallest_height

def test_sort():
    """Test that sort sorts."""
    # setup object to be tested
    initial_list = [20, 30, 10]
    sg = sortgui.SortGui(initial_list)
    # update sleep delay
    sg.search_input.insert(0, 0.001)
    sg.update_sleep(None)

    # sleep because of TK not being fast enough... this is a hack!!!
    import time
    time.sleep(1)

    # expected end rectangle heights
    initial_list.sort()
    expected_rectangle_heights = [value * sg.value_multiplier for value in initial_list]

    # actually sort rectangles
    sg.sort()

    # actual rectangle heights
    actual_rectangle_heights = []
    for rectangle_id in sg.rectangle_indices:
        # get height and append to actual height list
        current_height = sg.canvas.coords(rectangle_id)[3] - sg.canvas.coords(rectangle_id)[1]
        actual_rectangle_heights.append(current_height)

    assert actual_rectangle_heights == expected_rectangle_heights

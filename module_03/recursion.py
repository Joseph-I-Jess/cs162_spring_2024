
"""
5! = 120
5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4!

4! = 24
4! =     4 * 3 * 2 * 1
4! = 4 * 3!

3! = 3 * 2!

2! = 2 * 1!

1! = 1
"""

def fact(num):
    """Return factorial of num, or raise ValueError on negtaive values."""
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

# script part of code
invalid_input = True
while invalid_input == True:
    in_value = input("Please enter a non-negative whole number\n")
    try:
        in_value = int(in_value)
        # must have good integer value to get here...
        if in_value < 0:
            print(f"{in_value} is negative, which we do not want to deal with here, please try again.")
            # raise ValueError  # exception handling is valid as well!
        else:
            print(f"fact({in_value}): {fact(in_value)}")
            invalid_input = False
    except ValueError:
        print("N'ErRoR, are you an idiot...?")  # not nice🙁...

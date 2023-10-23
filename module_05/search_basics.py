import random

# create data
my_list = []
min_val = 0
max_val = 100

for i in range(10):
    my_list.append(random.randint(min_val, max_val + 1))

# debug, print list
print(f"my_list: {my_list}")

# ask the user for a value to search for
value = int(input(f"Please enter an integer from {min_val} through {max_val}: ")) # should have input validation

# check the list for that value one index at a time
for index,element in enumerate(my_list):
    # print(f"index: {index}, value: {element}")
    if value == element:
        print(f"found your value ({value}) at index: {index}")

# report to user where that value is in the list


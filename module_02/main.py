import Microwave

debug = False  # whether to print debug statements

my_nukerwave = Microwave.Microwave("Joseph's microwave", new_wattage=1100)
my_nukerwave_2 = Microwave.Microwave(2, "cubic meters", 1800, "watts")
print(f"my_nukerwave.volume: {my_nukerwave.volume} {my_nukerwave.volume_units}")
print(f"my_nukerwave.wattage: {my_nukerwave.wattage} {my_nukerwave.wattage_units}")

# my_nukerwave_2.volume = 2
# my_nukerwave_2.wattage = 1800
print(f"my_nukerwave_2.volume: {my_nukerwave_2.volume} {my_nukerwave_2.volume_units}")
print(f"my_nukerwave_2.wattage: {my_nukerwave_2.wattage} {my_nukerwave_2.wattage_units}")

my_nukerwave.upgrade()
# print(f"my_nukerwave.volume: {my_nukerwave.volume} {my_nukerwave.volume_units}")
# print(f"my_nukerwave.wattage: {my_nukerwave.wattage} {my_nukerwave.wattage_units}")
print(my_nukerwave)

filename = "microwave.config"
with open(filename, "w") as out_file:
    try:
        out_file.write(my_nukerwave.__str__())
        print(f"Successfully wrote contents of {filename}.")
    except FileNotFoundError:
        print("FileNotFoundError exception occurred, failed to write.")
    except:
        print("Some exception occurred, failed to write.")

filename_save = "microwave.sav"
with open(filename_save, "w") as out_file:
    try:
        out_file.write(repr(my_nukerwave))
        print(f"Successfully wrote contents of {filename_save}.")
    except FileNotFoundError:
        print("FileNotFoundError exception occurred, failed to write.")
    except:
        print("Some exception occurred, failed to write.")

# if instead we open outside of a with statement, we will also want to see a close
# out_file = open(...)
# out_file.close()

print(f"Attempting to open and read {filename}.")

with open(filename, "r") as in_file:
    lines = in_file.readlines()

print(lines)

# parse each attribute from file for a new microwave
name = lines[0][:-2]
# cheap, works for now, fix when needing more than one character
volume = int(lines[1][9])
volume_units = lines[1][11:-1]
power_line = lines[2].split(" ")
wattage = int(power_line[1])  # add input validation!
wattage_units = power_line[2]

if debug is True:
    print(name, volume, volume_units, wattage, wattage_units, sep="\n")

# create new microwave out of those parsed attributes
new_microwave = Microwave.Microwave(name, volume, volume_units, wattage, wattage_units)
print(new_microwave)
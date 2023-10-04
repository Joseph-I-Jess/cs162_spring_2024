"""Microwave class."""

debug = False  # whether to print debug statements


class Microwave:
    """Represents a Microwave object."""

    def __init__(self,
                 new_name: str = "unnamed microwave",
                 new_volume: int = 1,
                 new_volume_units: str = "cubic meters",
                 new_wattage: int = 1000,
                 new_wattage_units: str = "watts"):
        """Initialize a Microwave object."""
        self.name = new_name
        self.volume = new_volume
        self.volume_units = new_volume_units
        self.wattage = new_wattage
        self.wattage_units = new_wattage_units

    def upgrade(self):
        """Upgrade this Microwave."""
        self.volume *= 2
        self.wattage *= 2

    def __str__(self):
        """Represent this Microwave object as a string."""
        return f"{self.name}:\n" \
               f"\tvolume: {self.volume} {self.volume_units}\n" \
               f"\twattage: {self.wattage} {self.wattage_units}"


def test_default_microwave():
    m_wave = Microwave()

    expected_name = "unnamed microwave"
    expected_volume = 1
    expected_volume_units = "cubic meters"
    expected_wattage = 1000
    expected_wattage_units = "watts"

    assert expected_name == m_wave.name
    assert expected_volume == m_wave.volume
    assert expected_volume_units == m_wave.volume_units
    assert expected_wattage == m_wave.wattage
    assert expected_wattage_units == m_wave.wattage_units


# my_nukerwave = Microwave("Joseph's microwave", new_wattage=1100)
# my_nukerwave_2 = Microwave(2, "cubic meters", 1800, "watts")
# print(f"my_nukerwave.volume: {my_nukerwave.volume} {my_nukerwave.volume_units}")
# print(f"my_nukerwave.wattage: {my_nukerwave.wattage} {my_nukerwave.wattage_units}")

# # my_nukerwave_2.volume = 2
# # my_nukerwave_2.wattage = 1800
# print(f"my_nukerwave_2.volume: {my_nukerwave_2.volume} {my_nukerwave_2.volume_units}")
# print(f"my_nukerwave_2.wattage: {my_nukerwave_2.wattage} {my_nukerwave_2.wattage_units}")

# my_nukerwave.upgrade()
# # print(f"my_nukerwave.volume: {my_nukerwave.volume} {my_nukerwave.volume_units}")
# # print(f"my_nukerwave.wattage: {my_nukerwave.wattage} {my_nukerwave.wattage_units}")
# print(my_nukerwave)

# filename = "microwave.config"
# with open(filename, "w") as out_file:
#     try:
#         out_file.write(my_nukerwave.__str__())
#         print(f"Successfully wrote contents of {filename}.")
#     except FileNotFoundError:
#         print("FileNotFoundError exception occurred, failed to write.")
#     except:
#         print("Some exception occurred, failed to write.")

# # if instead we open outside of a with statement, we will also want to see a close
# # out_file = open(...)
# # out_file.close()

# print(f"Attempting to open and read {filename}.")

# with open(filename, "r") as in_file:
#     lines = in_file.readlines()

# print(lines)

# # parse each attribute from file for a new microwave
# name = lines[0][:-2]
# # cheap, works for now, fix when needing more than one character
# volume = int(lines[1][9])
# volume_units = lines[1][11:-1]
# power_line = lines[2].split(" ")
# wattage = int(power_line[1])  # add input validation!
# wattage_units = power_line[2]

# if debug is True:
#     print(name, volume, volume_units, wattage, wattage_units, sep="\n")

# # create new microwave out of those parsed attributes
# new_microwave = Microwave(name, volume, volume_units, wattage, wattage_units)
# print(new_microwave)

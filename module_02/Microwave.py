"""Implement a Microwave class."""

import random

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
        """Upgrade this Microwave with a random multiplier from 0-10."""
        self.volume *= random.randint(0, 10)
        self.wattage *= random.randint(0, 10)

    def __str__(self):
        """Represent this Microwave object as a string."""
        return f"{self.name}:\n" \
               f"\tvolume: {self.volume} {self.volume_units}\n" \
               f"\twattage: {self.wattage} {self.wattage_units}"

    def __repr__(self):
        return f"name: {self.name}\n" \
               f"volume: {self.volume}\n" \
               f"volume_units: {self.volume_units}\n" \
               f"wattage: {self.wattage}\n" \
               f"wattage_units: {self.wattage_units}"

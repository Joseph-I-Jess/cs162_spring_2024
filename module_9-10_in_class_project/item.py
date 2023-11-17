"""Represent an item in our game."""

class Item:
    """Represent an item in our game."""
    def __init__(self):
        self.id = 0
        self.name = "sword"
        self.description = "A sword..."
        self.stats = self.stats = {"attack":3, "defence": 0, "speed": 0, "health": 0}
        self.equipment = [] # for upgrades on the equipment
        self.inventory  = [] # if this item has an inventory...
        # add weight, volume, value, durability, ...?

    def __str__(self) -> str:
        result: str =  f"name: {self.name}:\n\t"
        result += f"description: {self.description}\n\t"
        
        result += f"stats:\n\t\t"
        for stat_name,stat in self.stats.items():
            result += f"{stat_name}: {stat}\n\t\t"
        result = result[:-1] # hack!
        
        result += f"equipment:\n\t"
        result += f"{self.equipment}\n\t"

        result += f"inventory:\n\t"
        result += f"{self.inventory}\n"

        return result

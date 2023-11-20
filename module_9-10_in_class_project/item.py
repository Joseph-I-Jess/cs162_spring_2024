"""Represent an item in our game."""

from __future__ import annotations

"""ToDo:
    add is_stackable, to be able to stack items in an inventory... do this purely by id in inventories?
"""

class Item:
    """Represent an item in our game."""
    def __init__(self,
                 id=0,
                 name="unnamed item",
                 description="undescribed item",
                 stats: dict[str, int]={"attack":0, "defence": 0, "speed": 0, "health": 0},
                 equipment: dict[str, Item] | None=None,
                 inventory: list[Item] | None=None,
                 is_equippable=False,
                 equipment_slot=None,
                 is_consumable=False,
                 is_upgradeable=False,
                 is_container=False,
                 is_equipped=False):
        self.id = id
        self.name = name
        self.description = description

        self.stats = stats

        if equipment is None:
            self.equipment: dict[str, Item] = {}
        else:
            self.equipment: dict[str, Item] = equipment # for upgrades on the equipment

        if inventory is None:
            self.inventory: list[Item] = []
        else:
            self.inventory: list[Item] = inventory # if this item has an inventory...

        # Note: anything equippable, MUST have an equipment slot
        self.is_equippable = is_equippable
        self.equipment_slot: str | None = equipment_slot
        if is_equippable is True and equipment_slot is None:
            print(f"N'Error! {name} is equippable but equipment slot is None!")

        self.is_consumable = is_consumable
        self.is_upgradeable = is_upgradeable
        self.is_container = is_container

        self.is_equipped = is_equipped

        # add weight, volume, value, durability, ...?

    def __str__(self) -> str:
        """Represent this as a human readable string."""
        result: str = f"Name: {self.name}"
        # add equipped tag to side of name
        if self.is_equipped is True:
            result += " (equipped)"
        result += ":\n"
        result += f"\tDescription: {self.description}\n"

        result += f"\tTags:\n"

        if self.is_equippable is True:
            result += f"\t\t(equipment)({self.equipment_slot})\n"

        if self.is_consumable is True:
            result += f"\t\t(consumable)\n"

        if self.is_upgradeable is True:
            result += f"\t\t(upgradeable)\n"

        if self.is_container is True:
            result += f"\t\t(container)\n"
        
        if self.is_equippable or self.is_consumable:
            result += f"\tStats:\n"
            for stat_name,stat in self.stats.items():
                result += f"\t\t{stat_name}: {stat}\n"
        
        if self.is_upgradeable:
            result += f"\tUpgrades:\n"
            if self.equipment is not None and len(self.equipment) > 0:
                result += f"______________begin of upgrades for {self.name}_______________\n"
                for equip_slot, equipped_item in self.equipment.items():
                    if equipped_item is not None:
                        result += f"{equip_slot}: {equipped_item.name} ("
                        for stat_name, stat_value in equipped_item.stats.items():
                            result += f"{stat_name}: {stat_value}, "
                        result = result[:-2] + ")\n" # hack to remove last comma!
                    else:
                        print("that equipped item is None...?")
                result += f"______________end of upgrades for {self.name}_______________\n"
            else:
                result += "\t\tNothing equipped.\n"

        if self.is_container:
            result += f"\tInventory:\n"
            if self.inventory is not None and len(self.inventory) > 0:
                result += f"__________begin inventory of {self.name}______________\n"
                for element in self.inventory:
                    result += f"{element}\n"
                result += f"__________end of inventory of {self.name}______________\n"
            else:
                result += "No items in inventory.\n"

        return result
    
    def add_item(self, item: Item | None=None):
        """Add item to this player's inventory if it is not None."""
        if self.is_container is True:
            if item is not None:
                self.inventory.append(item)
            else:
                print("that item is None, did you forget to pass an actual object into the add_item method?")
        else:
            print(f"{self.name} is not a container!")
    
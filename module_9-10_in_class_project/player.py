"""Represent a player in our game."""

import item

class Player():
    """Represent a player in our game."""
    def __init__(self,
                 id=0,
                 name="unnamed player",
                 description="undescribed player",
                 stats: dict[str, int]={"attack":0, "defence": 0, "speed": 0, "health": 0},
                 equipment: dict[str, item.Item] | None=None,
                 inventory: list[item.Item] | None=None,
                 experience=0,
                 level=1
                 ):
        self.id = id
        self.name = name
        self.description = description
        # maybe we should make a stats class to handle complex issues with stat representation....
        # self.valid_stats = ["attack", "defence", "speed", "health"]
        self.stats = stats

        if equipment is None:
            self.equipment: dict[str, item.Item] = {}
        else:
            self.equipment: dict[str, item.Item] = equipment # for upgrades on the equipment

        if inventory is None:
            self.inventory: list[item.Item] = []
        else:
            self.inventory: list[item.Item] = inventory # if this item has an inventory...

        self.experience = experience
        self.level = level

    def __str__(self) -> str:
        result: str =  f"Name: {self.name}:\n"
        result += f"\tDescription: {self.description}\n"
        
        result += f"\tStats:\n"
        for stat_name,stat in self.stats.items():
            result += f"\t\t{stat_name}: {stat}\n"
        
        result += f"\tEquipment:\n"
        if len(self.equipment) > 0:
            result += f"_____________begin of equipment for {self.name}________________\n"
            for equip_slot, equipped_item in self.equipment.items():
                if equipped_item is not None:
                    result += f"{equip_slot}: {equipped_item.name} ("
                    for stat_name, stat_value in equipped_item.stats.items():
                        result += f"{stat_name}: {stat_value}, "
                    result = result[:-2] + ")\n" # hack to remove last comma!
                else:
                    print("that equipped item is None...?")
            result += f"_____________end of equipment for {self.name}________________\n"
        else:
            result += "\t\tNothing equipped.\n"
        
        result += f"\tInventory:\n"
        if len(self.inventory) > 0:
            result += f"_____________begin of inventory of {self.name}________________\n"
            for element in self.inventory:
                result += f"{element}\n"
            result += f"_____________end of inventory of {self.name}________________\n"
        else:
            result += "No items in inventory.\n"

        return result
    
    def add_item(self, item: item.Item | None=None):
        """Add item to this player's inventory if it is not None."""
        if item is not None:
            self.inventory.append(item)

    def equip(self, item_proposed: item.Item | None=None):
        """Attempt to equip item on this player, taking into account equipment slots..."""
        if item_proposed is not None:
            if item_proposed.is_equipped is False:
                # check if that slot is already in use, if so, unequip that item first!
                if item_proposed.is_equippable is True and item_proposed.equipment_slot is not None:
                    # check equipped items for unequipment only if that slot is already in use (not None)
                    if item_proposed.equipment_slot in self.equipment:
                        current_equip: item.Item | None = self.equipment[item_proposed.equipment_slot]
                        if current_equip is not None:
                            # unequip old item and reduce stats first!
                            del self.equipment[item_proposed.equipment_slot]
                            current_equip.is_equipped = False
                            for item_stat_name,item_stat in current_equip.stats.items():
                                self.stats[item_stat_name] -= item_stat
                    # actually label as equipped and add stats
                    self.equipment[item_proposed.equipment_slot] = item_proposed
                    item_proposed.is_equipped = True
                    for item_stat_name,item_stat in item_proposed.stats.items():
                        self.stats[item_stat_name] += item_stat
                else:
                    print(f"{item_proposed.name}({item_proposed.equipment_slot}) is not equippable")
            else:
                print(f"{item_proposed.name} is already equipped, did you mean to unequip it?")
        else:
            print("That item is None, you cannot equip it, did you forget to pass an actual item to the equip method?")

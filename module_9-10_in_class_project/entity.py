"""Represents the abstract similarities among beings, items, maps, and other game entities."""

from __future__ import annotations

import item

class Entity:
    """An "abstract" class that contains common attributes among different game entities."""

    def __init__(self,
                 id: int=0,
                 name: str="unnamed player",
                 description: str="undescribed player",
                 stats: dict[str, int]={},
                 equipment: dict[str, item.Item] | None=None,
                 inventory: list[item.Item] | None=None,) -> None:
        """Initialize this "object", likely only used to set base values for subclasses."""
        self.id: int = id
        self.name: str = name
        self.description: str = description
        # maybe we should make a stats class to handle complex issues with stat representation....
        self.valid_stats: list[str] = ["attack", "defence", "speed", "health"]
        self.stats: dict[str, int] = stats

        if equipment is None:
            self.equipment: dict[str, item.Item] = {}
        else:
            self.equipment: dict[str, item.Item] = equipment # for upgrades on the equipment

        if inventory is None:
            self.inventory: list[item.Item] = []
        else:
            self.inventory: list[item.Item] = inventory # if this item has an inventory...

    def __str__(self, additional_attributes_categorical_names: list[str | None] | None=None, additional_attributes_list: list[list[tuple[str, str]]] | None=None) -> str:
        """Human readable formatted data of this object.
        
            @param: additional_attributes is a dictionary where keys are the name of an attribute to be added and the values are the value associated with that added attribute.
        """
        result: str =  f"Name: {self.name}:\n"
        result += f"\tDescription: {self.description}\n"
        
        # if no additional attributes, then do not print anything else
        if additional_attributes_list is not None:
            # if categorical names exist, then use them with the additional attributes lists
            additional_attributes_tab_level: str = "\t"
            if additional_attributes_categorical_names is not None:
                for count in range(len(additional_attributes_list)):
                    if count < len(additional_attributes_categorical_names):
                        additional_attributes_categorical_name: str | None = additional_attributes_categorical_names[count]
                    else:
                        additional_attributes_categorical_name = None
                    additional_attributes: list[tuple[str, str]] = additional_attributes_list[count]
                    # reset, as each list might or might not have a categorical name
                    additional_attributes_tab_level = "\t"
                    # if categorical name is not none, then increase tab level to nest under categorical name
                    if additional_attributes_categorical_name is not None:
                        result += f"{additional_attributes_tab_level}{additional_attributes_categorical_name}:\n"
                        # increase tab level if we have a categorical name
                        additional_attributes_tab_level += "\t"
                    if additional_attributes is not None:
                        for attribute_name, attribute_value in additional_attributes:
                            result += f"{additional_attributes_tab_level}"
                            if attribute_name is not None:
                                result += f"{attribute_name}: "
                            if attribute_value is not None:
                                result += f"{attribute_value}\n"
            # otherwise, just print all additional attributes one level under character
            else:
                for additional_attributes in additional_attributes_list:
                    for attribute_name, attribute_value in additional_attributes:
                            result += f"{additional_attributes_tab_level}{attribute_name}: {attribute_value}\n"

        if len(self.stats) > 0:
            result += f"\tStats:\n"
            for stat_name,stat in self.stats.items():
                result += f"\t\t{stat_name}: {stat}\n"
        
        if len(self.equipment) > 0:
            result += f"\tEquipment:\n"
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
        
        if len(self.inventory) > 0:
            result += f"\tInventory:\n"
            result += f"_____________begin of inventory of {self.name}________________\n"
            for element in self.inventory:
                result += f"{element}\n"
            result += f"_____________end of inventory of {self.name}________________\n"

        return result
    
    def add_item(self, item: item.Item | None=None) -> str:
        """Add item to this Entity's inventory if it is not None."""
        result = ""
        if item is not None:
            self.inventory.append(item)
            result += f"{item.name} has been added to {self.name}'s inventory."
        else:
            result += "that item is None, did you forget to pass an actual object into the add_item method?"
        
        return result
    
    def equip(self, item_proposed: item.Item | None=None):
        """Attempt to equip item on this player, taking into account equipment slots..."""
        result: str = ""
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
                    result = f"{item_proposed.name}({item_proposed.equipment_slot}) is not equippable"
            else:
                result = f"{item_proposed.name} is already equipped, did you mean to unequip it?"
        else:
            result = "That item is None, you cannot equip it, did you forget to pass an actual item to the equip method?"

        return result

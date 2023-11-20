"""Represent an item in our game."""

from __future__ import annotations

import entity

"""ToDo:
    add is_stackable, to be able to stack items in an inventory... do this purely by id in inventories?
"""

class Item(entity.Entity):
    """Represent an item in our game."""
    def __init__(self,
                 id: int=0,
                 name: str="unnamed item",
                 description: str="undescribed item",
                 stats: dict[str, int]={},
                 equipment: dict[str, Item] | None=None,
                 inventory: list[Item] | None=None,
                 is_equippable: bool=False,
                 equipment_slot: str | None=None,
                 is_consumable: bool=False,
                 is_upgradeable: bool=False,
                 is_container: bool=False,
                 is_equipped: bool=False) -> None:
        super().__init__(id, name, description, stats, equipment, inventory)

        # Note: anything equippable, MUST have an equipment slot
        self.is_equippable: bool = is_equippable
        self.equipment_slot: str | None = equipment_slot
        if is_equippable is True and equipment_slot is None:
            print(f"N'Error! {name} is equippable but equipment slot is None!")

        self.is_consumable: bool = is_consumable
        self.is_upgradeable: bool = is_upgradeable
        self.is_container: bool = is_container

        self.is_equipped: bool = is_equipped

        # add weight, volume, value, durability, ...?

    def __str__(self) -> str:
        """Represent this as a human readable string."""
        additional_attributes_catigorical_names = []
        additional_attributes_list =[]
        
        # add equipped tag to side of name
        additional_attributes_catigorical_names.append(None)
        if self.is_equipped is True:
            additional_attributes_list.append([(None, "(Equipped)")])
        else:
            additional_attributes_list.append(None)
        
        
        #additional item tags
        additional_attributes: list[tuple[str | None, str | None]] = []
        if self.is_equippable is True:
            additional_attributes.append(("equipment", self.equipment_slot))

        if self.is_consumable is True:
            additional_attributes.append((None, "(consumable)")) # list uses remaining?

        if self.is_upgradeable is True:
            additional_attributes.append((None, "(upgradeable)")) # list upgrade slots used and available?

        if self.is_container is True:
            additional_attributes.append((None, "(container)")) # list capacity used and available?

        # only add the tags categorical name if at least one tag exists and append additional_attributes as well
        if len(additional_attributes) > 0:
            additional_attributes_catigorical_names.append("Tags")
            additional_attributes_list.append(additional_attributes)
            

        return super().__str__(additional_attributes_catigorical_names, additional_attributes_list)
    
    def add_item(self, item: Item | None=None) -> str:
        """Add item to this player's inventory if it is not None."""
        result: str = ""
        if self.is_container is True:
            result = super().add_item(item)
        else:
            result = f"{self.name} is not a container!"

        return result
    
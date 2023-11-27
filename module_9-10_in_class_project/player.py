"""Represent a player in our game."""

from __future__ import annotations

import entity
import item

class Player(entity.Entity):
    """Represent a player in our game."""
    def __init__(self,
                 id: int=0,
                 name: str="unnamed player",
                 description: str="undescribed player",
                 stats: dict[str, int]={"attack":0, "defence": 0, "speed": 0, "health": 0, "experience": 0},
                 equipment: dict[str, item.Item] | None=None,
                 inventory: list[item.Item] | None=None,
                 level: int=1
                 ) -> None:
        super().__init__(id, name, description, stats, equipment, inventory)

        self.level_name = "level"
        self.level: int = level

    # customize to also include level and experience?
    def __str__(self) -> str:
        return super().__str__(additional_attributes_list=[[(self.level_name,str(self.level))]])
        

    # do we need a customized equip method?

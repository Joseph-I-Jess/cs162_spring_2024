"""Represent a player in our game."""

from __future__ import annotations

import item
import being
import map_cell

class Player(being.Being):
    """Represent a player in our game."""
    def __init__(self,
                 id: int=0,
                 name: str="unnamed player",
                 description: str="undescribed player",
                 stats: dict[str, int]={"attack":0, "defence": 0, "speed": 0, "health": 0, "experience": 0},
                 equipment: dict[str, item.Item] | None=None,
                 inventory: list[item.Item] | None=None,
                 location: map_cell.MapCell | None=None,
                 level: int=1
                 ) -> None:
        super().__init__(id, name, description, stats, equipment, inventory, location)

        self.level_name = "level"
        self.level: int = level

    # customize to also include level and experience?
    def __str__(self) -> str:
        return super().__str__(additional_attributes_list=[[(self.level_name,str(self.level))]])
        
    def move(self, direction:str)-> str:
        """Attempt to move in a given direction based on the current location."""
        result: str = ""

        if self.location is not None:
            exits: dict[str, map_cell.MapCell] = self.location.exits
            if direction in exits.keys():
                destination: map_cell.MapCell = exits[direction]
                result = f"{self.name} moved from {self.location.name} to {destination.name} via {direction}"
                self.location = destination
    
        return result

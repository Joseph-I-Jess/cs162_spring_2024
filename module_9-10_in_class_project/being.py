"""Represent beings in this game."""

from __future__ import annotations

import entity
import item
# import map_cell # import map_cell causes circular import, even though it is only used for type hints

class Being(entity.Entity):
    """A being in this game..."""
    def __init__(self,
                 id: int=0,
                 name: str="unnamed enemy",
                 description: str="undescribed enemy",
                 stats: dict[str, int]={"attack":0, "defence": 0, "speed": 0, "health": 0},
                 equipment: dict[str, item.Item] | None=None,
                 inventory: list[item.Item] | None=None,
                 location=None
                 ) -> None:
        super().__init__(id, name, description, stats, equipment, inventory, location)

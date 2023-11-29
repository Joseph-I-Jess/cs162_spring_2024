"""Represent a single space in a room, which can hold items, enemies, players, and possibly other game objects such as walls, floors, and ceilings."""

from __future__ import annotations

import entity
import item
import enemy
import player

class MapCell(entity.Entity):
    """Represent one space in a map."""
    def __init__(self, id: int=0,
                 name: str="unnamed map cell",
                 description: str="undescribed map cell",
                 stats: dict[str, int]={},
                 equipment: dict[str, item.Item] | None=None,
                 inventory: list[item.Item] | None=None, # holds items
                 exits: dict[str, MapCell]={}, # string is exit direction from this MapCell to a destination MapCell
                 players: list[player.Player]=[],
                 enemies: list[enemy.Enemy]=[]
                ) -> None:
        super().__init__(id, name, description, stats, equipment, inventory)

        # create empty lists if needed at creation time
        if exits == {}:
            self.exits: dict[str, MapCell] = {}
        else: 
            self.exits: dict[str, MapCell] = exits

        if exits == []:
            self.players: list[player.Player] = []
        else:
            self.players: list[player.Player] = players

        if exits == []:
            self.enemies: list[enemy.Enemy] = []
        else:
            self.enemies: list[enemy.Enemy] = enemies

    def __str__(self) -> str:
        """Print both normal entity attributes and custom attributes of self (exits, players, and enemies)."""
        additional_attributes_categorical_names: list[str | None] | None = []
        additional_attributes_list: list[list[tuple[str | None, str | None]]] = []
        
        # print exits if they exist
        if len(self.exits.keys()) > 0:
            additional_attributes_categorical_names.append("exits")
            exits_list: list[tuple[str | None, str | None]] = []
            for exit_direction, destination in self.exits.items():
                exits_list.append((exit_direction, destination.name))
            additional_attributes_list.append(exits_list)

        # print player names if players exist
        if len(self.players) > 0:
            additional_attributes_categorical_names.append("players")
            players_list: list[tuple[str | None, str | None]] = []
            for player in self.players:
                players_list.append((None, player.name))
            additional_attributes_list.append(players_list)

        # print enemy names if enemies exist
        if len(self.enemies) > 0:
            additional_attributes_categorical_names.append("enemies")
            enemies_list: list[tuple[str | None, str | None]] = []
            for enemy in self.enemies:
                enemies_list.append((None, enemy.name))
            additional_attributes_list.append(enemies_list)

        result: str = super().__str__(additional_attributes_categorical_names, additional_attributes_list)

        return result

    def add_exit(self, exit_direction: str, destination: MapCell) -> str:
        """Add an exit to self with direction of exit_direction and a destination of destination."""
        result: str = ""

        valid_input = True
        if exit_direction == "" or exit_direction == None:
            result += "Neither an empty string nor a None type are allowed for an exit direction."
            valid_input = False
        if destination is None:
            result += "A None type is not allowed for an exit destination."
            valid_input = False

        if valid_input is True:
            self.exits[exit_direction] = destination
            result += f"\tAn exit has been added from {self.name} to {destination.name} via {exit_direction}.\n"

        return result

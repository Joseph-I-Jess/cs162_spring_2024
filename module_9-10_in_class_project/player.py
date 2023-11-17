"""Represent a player in our game."""

class Player():
    """Represent a player in our game."""
    def __init__(self):
        self.id = 0
        self.name = "No name"
        self.description = "No description yet"
        # maybe we should make a stats class to handle complex issues with stat representation....
        # self.valid_stats = ["attack", "defence", "speed", "health"]
        # self.attack = 10 # bonus damage
        # self.defence = 5 # damage reduction
        # self.speed = 5 # initiative, or should we switch to rock-paper-scissors?
        # self.health = 20 # total damage before loss of consciousness
        self.stats = {"attack":10, "defence": 5, "speed": 5, "health": 20}
        self.equipment = []
        self.inventory = []
        self.experience = 0
        self.level = 1

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

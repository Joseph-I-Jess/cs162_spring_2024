import item
import player

"""ToDo:
    decide on in-class project (example final project)
        text-based RPG with graphical view (try to create both a top-down map view and a first-person view?)
    design in-class project
        - entity?    
            - being:
                - player (attack, defense, special ability bar (timer?))
                - enemy (should they move, patrol or random, should they follow the player after seeing or engaging in combat with them, ...?)
                - combat system, experience, equipment system
            - item: items, weapons, armors, currencies
            - map
                - room (description, enemies, players, inventory on ground?, exits; might have conditions on seeing full description, enemies, players, inevtory?, and exits)
                    - map_cell (floor, wall, ceiling, inventory?)
                        - floor
                        - wall(s)
                        - ceiling
        - inventory (for both beings, but also environmental things such as treasure chests or other containers)
                - holds items... including other inventories...?
        - command interpreter!
        - GUI
            - stuff...!
    start to implement project

    update design to project...

    continue to implement project...

    ...
"""

def main():
    p1 = player.Player()

    print(f"p1:\n_____________________________\n{p1}_____________________________\n")

    p2 = player.Player()
    p2.name = "Joseph"
    p2.description = "A 37 year old CS instructor stares into the void with a blank look on their face..."
    p2.stats["attack"] = 7

    print(f"p2:\n_____________________________\n{p2}_____________________________\n")

    item_1 = item.Item()
    print(f"item_1:\n_____________________________\n{item_1}_____________________________\n")

if __name__ == "__main__":
    main()

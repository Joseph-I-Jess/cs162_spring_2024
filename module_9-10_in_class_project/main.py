from __future__ import annotations

# import primitives first!
import item

# import complex classes after primitives
import enemy
import player

"""ToDo:
    decide on in-class project (example final project)
        text-based RPG with graphical view (try to create both a top-down map view and a first-person view?)
    design in-class project
        - entity
            -- .maybe change additional attributes of the __str__ method to be a list of categories and a list of list of tuple of (str, str)?
            - being:
                - .player (attack, defense, special ability bar (timer?))
                  -- consider removing equipment and inventory from __init__...
                - enemy (should they move, patrol or random, should they follow the player after seeing or engaging in combat with them, ...?)
                -- combat system, experience, equipment system
            - item: items, weapons, armors, currencies
                - .can be equippable (equipment)
                    - .equipment slot (weapon, armor, accessory)
                - can be consumable (consumable)
                - can be upgradeable (upgrade; equipment of equipment)
                - can have an inventory (container; can contain other items)
                    - has a capacity?
            - map
                - room (description, enemies, players, inventory on ground?, exits; might have conditions on seeing full description, enemies, players, inevtory?, and exits)
                    - map_cell (floor, wall, ceiling, inventory?)
                        - floor
                        - wall(s)
                        - ceiling
                        !-- have defeated enemies drop items onto map_cell floor, rather than directly into player inventory (go modify entity.Entity.attack method!)
        - inventory (for both beings, but also environmental things such as treasure chests or other containers)
                - .for players
                - .for items
                - for map_cells
        - command interpreter!
        - GUI
            -- stuff...!
    start to implement project
        .

    update design to project...

    continue to implement project...

    ...
"""

def main():
    # create a player
    p1 = player.Player()

    #print that player
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")



    #create another player to show that players are distinct from each other
    p2 = player.Player()
    p2.name = "Joseph"
    p2.description = "A 37 year old CS instructor stares into the void with a blank look on their face..."
    p2.stats["attack"] = 7

    # print that second player
    print(f"p2:\n___________________________________________________________\n{p2}___________________________________________________________\n")



    # create an item and print it out
    item_1 = item.Item(name="sword", description="a simple sword", is_equippable=True, equipment_slot="weapon", stats={"attack":3})
    print(f"item_1:\n_________________________________________________\n{item_1}_________________________________________________\n")



    # add item to player inventory and reprint player
    print("adding item to player inventory.")
    p1.add_item(item_1)
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")



    # equip item to player and reprint player to show equipped item
    print(f"equipping item {item_1.name} to player inventory.")
    p1.equip(item_1)
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")



    # create a new item and add to player inventory and print player to show that it is not equipped
    item_2 = item.Item(name="hammer", description="a simple hammer", is_equippable=True, equipment_slot="weapon", stats={"attack":4})
    print(f"item_2:\n_________________________________________________\n{item_2}_________________________________________________\n")
    print("adding item to player inventory.")
    p1.add_item(item_2)
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")

    # (fixed, yay!) show that we can currently equip an item multiple times!!!
    # print(f"equipping item {item_1.name} to player inventory a second time!")
    # p1.equip(item_1)
    # print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")
    # print(f"equipping item {item_1.name} to player inventory a third time!")
    # p1.equip(item_1)
    # print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")

    # (fixed multiple items of the same equipment slot, yay!) show that we can equip multiple items of a similar equipment slot
    print(f"equipping item {item_2.name} to player inventory!")
    p1.equip(item_2)
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")

    # create some armor just to make sure that all works with different equipment slots!
    print("Equipping armor") 
    item_armor = item.Item(name="leather armor", description="simple leather armor", is_equippable=True, equipment_slot="armor", stats={"defence":2})
    p1.add_item(item_armor)
    p1.equip(item_armor)
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")

    # create some accessory just to make sure that all works with different equipment slots!
    print("Equipping accessory") 
    item_accessory = item.Item(name="ring of power", description="the one ring", is_equippable=True, equipment_slot="accessory", stats={"attack":2, "defence":2, "speed":2, "health":10})
    p1.add_item(item_accessory)
    print(f"result from: p1.equip(item_accessory): {p1.equip(item_accessory)}")
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")



    # create a bag with some coins!
    print("Creating coins, bag, and adding coins to bag!")
    item_coin = item.Item(name="coins", description="a stack of coins")
    item_bag = item.Item(name="cloth sack", description="a cloth sack", is_container=True)
    item_bag.add_item(item_coin)
    p1.add_item(item_bag)
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")

    # create another bag with some coins and put it in the first bag!
    print("Creating more coins, another bag, and adding coins to bag and adding bag to previous bag!")
    item_coin2 = item.Item(name="more coins", description="a stack of coins")
    item_bag2 = item.Item(name="another cloth sack", description="a cloth sack", is_container=True)
    item_bag2.add_item(item_coin2)
    item_bag.add_item(item_bag2)
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")
    # # debug to find recursion... they had a shared inventory due to default parameters for an empty list being *the same* list that got created at definition time
    # print(f"item_coin2: {item_coin2}")
    # print(f"item_bag2: {item_bag2}")

    # # did p1 and p2 have a shared inventory!?!  They did once I added deafult parameters of {} or [] (empty dictionary or empty list as default parameter means all instances share the same initially-empty dictionary or list)
    # print(f"p2:\n___________________________________________________________\n{p2}___________________________________________________________\n")

    e1 = enemy.Enemy(name="goblin", description="a small weak goblin", stats={"attack": 5, "defence": 1, "health": 9, "experience": 1})
    print(f"e1:\n___________________________________________________________\n{e1}___________________________________________________________\n")
    # test positive attack case
    # print(f"results from first p1.attack(e1): {p1.attack(e1)}")
    # print(f"results from second p1.attack(e1): {p1.attack(e1)}")

    # (fixed!) test attack case where target has no defence stat
    # print(f"results from p1.attack(item_coin): {p1.attack(item_coin)}")

    # simulate continuous combat
    rounds = 0
    while p1.stats["health"] > 0 and e1.stats["health"] > 0:
        rounds += 1
        print(f"round {rounds}")
        print(p1.fight(e1))
    # end combat simulation

    # verify experience award
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")    
    
    # create another enemy, this time with an item
    item_dagger = item.Item(name="dagger", description="a tiny dagger", is_equippable=True, equipment_slot="weapon", stats={"attack":1})
    item_coin3 = item.Item(name="yet more coins", description="another stack of coins")
    e2 = enemy.Enemy(name="goblin", description="a small weak goblin", stats={"attack": 5, "defence": 1, "health": 9, "experience": 1}, inventory=[item_dagger])
    e2.add_item(item_coin3)
    e2.equip(item_dagger)

    # simulate continuous combat again?
    rounds = 0
    while p1.stats["health"] > 0 and e2.stats["health"] > 0:
        rounds += 1
        print(f"round {rounds}")
        print(p1.fight(e2))
    # end combat simulation

    # verify experience and item award again!?!
    print(f"p1:\n___________________________________________________________\n{p1}___________________________________________________________\n")    
    print(f"e2:\n___________________________________________________________\n{e2}___________________________________________________________\n")    

if __name__ == "__main__":
    main()

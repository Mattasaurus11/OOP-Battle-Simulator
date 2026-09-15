from monster import Monster
from hunter import Hunter
from time import sleep

ARENA_NAME = "Dimensional Crack"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to the dungeon of the {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gate is opening...")

    enemies = []
    monster = Monster("Beast Monarch")
    enemies.append(monster.name)
    monster2 = Monster("Insect Monarch")
    enemies.append(monster2.name)
    monster3 = Monster("Frost Monarch")
    enemies.append(monster3.name)
    sleep(0.5)

    

    print(f"{monster.name} enters the dungeon with {monster.health} health.")
    print(f"{monster2.name} enters the dungeon with {monster2.health} health.")
    print(f"{monster3.name} enters the dungeon with {monster3.health} health.")
    print("But no hunter has answered the call... yet.")
    sleep(0.5)

    hunter = Hunter(input("What is the Hunters Name: "))
    sleep(0.5)

    while hunter.is_alive():
            if monster.is_alive():
                attackedMonsterHealth = monster.take_damage(hunter.attack())
                sleep(0.5)
                print("Since monster is still alive it attacks hunter")
                sleep(0.5)
                attackedHunterHealth = hunter.take_damage(monster.attack())
                sleep(0.5)
            else:
                if monster2.is_alive():
                    attackedMonsterHealth = monster2.take_damage(hunter.attack())
                    sleep(0.5)
                    print("Since monster is still alive it attacks hunter")
                    sleep(0.5)
                    attackedHunterHealth = hunter.take_damage(monster2.attack())
                    sleep(0.5)
                else:
                    if monster3.is_alive():
                        attackedMonsterHealth = monster3.take_damage(hunter.attack())
                        sleep(0.5)
                        print("Since monster is still alive it attacks hunter")
                        sleep(0.5)
                        attackedHunterHealth = hunter.take_damage(monster3.attack())
                        sleep(0.5)
                    else:
                        print(f"Hunter has won the battle against {enemies}")
                        sleep(0.5)
                        return True
            print(f"{enemies} has won the battle")

if __name__ == "__main__":
    main()

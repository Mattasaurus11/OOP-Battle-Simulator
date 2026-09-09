from goblin import Goblin


ARENA_NAME = "Mandarin2"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to the classroom of {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The doors are opening...")

    goblin = Goblin("Characters")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no teacher has answered the call... yet.")


if __name__ == "__main__":
    main()

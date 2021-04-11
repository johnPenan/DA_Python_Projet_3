from logic.labyrinth import Labyrinth
from logic.macgyver import MacGyver

directions = {
    "h": "go_up",
    "b": "go_down",
    "d": "go_right",
    "g": "go_left"
}

def main():
    labyrinth = Labyrinth()
    labyrinth.load_labyrinth_from_file("resources/labyrinth.txt")
    macgyver = MacGyver(labyrinth)

    running = True

    while running:
        print(labyrinth.display())
        response = input("Where do you want to go ? ( Q to quit the game)").lower()
        if response == "q":
            running = False
        elif response in ("h", "b", "d", "g"):
            running = macgyver.move(directions[response])

if __name__=="__main__":
    main()    
    

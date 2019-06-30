from labyrinth import Labyrinth
from macGyver import MacGyver

def main():
    labyrinth = Labyrinth()
    mac = MacGyver(labyrinth)
    print("Hello", mac)

if __name__=="__main__":
    main()    
    

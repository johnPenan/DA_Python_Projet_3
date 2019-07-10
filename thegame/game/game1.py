import pygame as pg 

from ..config import settings

class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.background = pg.image.load(settings.BACKGROUND).convert()
        self.screen.blit(self.background, (0, 0))

        pg.display.update()

        self.running = False

        
    def start(self):
        self.running = True

        # Démarrage de la boucle de jeu
        while self.running:
            pg.event.pump()
            response = input("Enter quit to exit the program:").lower()
            if response == "quit":
                self.running = False          


def main():
    game = Game()
    game.start()

if __name__=="__main__":
    main()

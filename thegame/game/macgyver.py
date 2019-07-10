import pygame as pg 

from ..config import settings

class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.background = pg.image.load(settings.BACKGROUND).convert()
        self.screen.blit(self.background, (0, 0))

        self.macgyver = pg.image.load(settings.MACGYVER).convert_alpha()
        #self.macgyver.set_colorkey(settings.BLACK) To remove the black color in the image
        self.screen.blit(self.macgyver, (0, 0))

        pg.display.update()

        self.running = False

        
    def start(self):
        self.running = True

        # Démarrage de la boucle de jeu
        while self.running:
            for event in pg.event.get(pg.QUIT):
                self.running = False
                pg.display.update()
                   


def main():
    game = Game()
    game.start()

if __name__=="__main__":
    main()

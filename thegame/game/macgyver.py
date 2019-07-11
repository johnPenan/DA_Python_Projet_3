import pygame as pg 

from ..config import settings

class Game:

    def __init__(self):
        """Initialization of pygame library """
        pg.init()
        # Definition of Labyrinth screen
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # Load Labyrinth background
        self.background = pg.image.load(settings.BACKGROUND).convert()
        # Place background on the screen
        self.screen.blit(self.background, (0, 0))
        #Load macgyver image
        self.macgyver = pg.image.load(settings.MACGYVER).convert_alpha()
        #self.macgyver.set_colorkey(settings.BLACK) To remove the black color in the image
        #Place macgyver on the Labyrinth screen
        self.screen.blit(self.macgyver, (0, 0))
        #Load gardien image
        self.gardien = pg.image.load(settings.GARDIEN).convert_alpha()
        #Place gardien image on the Labyrinth screen
        self.screen.blit(self.gardien, (10,10))
        # update all Labyrinth screen
        pg.display.update()

        self.running = False

        
    def start(self):
        """This method launch Labyrinth game"""
        self.running = True
        # Start game running
        while self.running:
            for event in pg.event.get(pg.QUIT):
                self.running = False
                pg.display.update()
                   


def main():
    game = Game()
    game.start()

if __name__=="__main__":
    main()

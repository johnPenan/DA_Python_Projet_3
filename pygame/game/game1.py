import pygame as pg 

from ..config import settings

class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(settings.WIDTH, settings.HEIGHT)
        self.background = pg.image.load(settings.BACKGROUND).convert()
        self.screen.blit(self.background, (0, O))

        pg.display.update()

        self.running = False

        
    def start(self):
        pass




# def main():
#     game = Game()
#     game.start()

# if __name__="__main__":
#     main()


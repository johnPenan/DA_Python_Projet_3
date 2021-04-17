
import pygame

pygame.init()

from logic.labyrinth import Labyrinth
from logic.macgyver import MacGyver

class Game:
    ''' Game to help MacGyver escape '''
    def __init__(self):
        
        self.window_resolution = (600, 600)
        self.streets = pygame.image.load("stage/streets.png")
        self.walls = pygame.image.load("stage/murs.png")
        self.game_is_running = True
        self.blank_color = (0, 0, 0)
        self.labyrinth = Labyrinth()
        self.labyrinth.load_labyrinth_from_file("resources/labyrinth.txt")
        self.macgyver = MacGyver(self.labyrinth)

    def display(self):

        pygame.display.set_caption("Labyrinth Game")
        window_surface = pygame.display.set_mode(self.window_resolution, pygame.RESIZABLE)

        while self.game_is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False

            window_surface.fill(self.blank_color)
            for wall in self.labyrinth.walls:
                window_surface.blit(self.walls, [wall.x*40, wall.y*40])
            """window_surface.blit(self.streets, [10, 10])
            window_surface.blit(self.walls, [40, 40])
            """
            pygame.display.flip()



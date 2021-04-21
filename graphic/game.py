
import pygame

pygame.init()

from logic.labyrinth import Labyrinth
from logic.macgyver import MacGyver
from logic.position import Position

class Game:
    ''' Game to help MacGyver escape '''
    def __init__(self):
        
        self.window_resolution = (600, 600)
        self.streets = pygame.image.load("stage/streets.png")
        self.walls = pygame.image.load("stage/walls.png")
        self.departure = pygame.image.load("stage/departure.png")
        self.arrival = pygame.image.load("stage/arrival.png")
        self.hero = pygame.image.load("stage/macGyver.png")
        self.needle = pygame.image.load("stage/needle.png")
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
            for street in self.labyrinth.streets:
                window_surface.blit(self.streets, [street.x*40, street.y*40])
            # walls
            for wall in self.labyrinth.walls:
                window_surface.blit(self.walls, [wall.x*40, wall.y*40])
            # departure
            for street in self.labyrinth.streets:
                    window_surface.blit(self.departure, [self.labyrinth.departure.x, self.labyrinth.departure.y]) 
            # arrival or gardien
            for street in self.labyrinth.streets:
                    window_surface.blit(self.arrival, [self.labyrinth.arrival.x, self.labyrinth.arrival.y])  
            # macgyver
            for street in self.labyrinth.streets:
                window_surface.blit(self.hero, [self.macgyver.position.x, self.macgyver.position.y]) 
            # needle
            for ob in self.labyrinth.object_positions:
                window_surface.blit(self.needle, [ob.x, ob.y]) 
            pygame.display.flip()



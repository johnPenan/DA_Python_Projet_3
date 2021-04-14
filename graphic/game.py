
import pygame

pygame.init()

class Game:
    ''' Game to help MacGyver escape '''
    def __init__(self):
        self.window_resolution = (600, 600)
        self.streets = pygame.image.load("../stage/streets.png")
        self.walls = pygame.image.load("../stage/walls.png")
        self.game_is_running = True
        self.blank_color = (0, 0, 0)

    def display(self):

        pygame.display.set_caption("Macgyver Labyrinth Game")
        window_surface = pygame.display.set_mode(self.window_resolution, pygame.RESIZABLE)

        while self.game_is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False

            window_surface.fill(self.blank_color)
            window_surface.blit(self.streets, [10, 10])
            window_surface.blit(self.walls, [40, 40])
            pygame.display.flip()


game = Game()
game.display()
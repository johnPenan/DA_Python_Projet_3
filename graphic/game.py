import pygame

from logic.labyrinth import Labyrinth
from logic.macgyver import MacGyver
from logic.object import Object
from resources import constants

pygame.init()


class Game:
    """Game to help MacGyver escape"""

    def __init__(self):
        """ This method is the constructor of Game class """
        self.game_is_running = True
        self.labyrinth = Labyrinth()
        self.labyrinth.load_labyrinth_from_file("resources/labyrinth.txt")
        self.macgyver = MacGyver(self.labyrinth)
        self.objects = []
        for i in range(3):
            self.objects.append(
                Object(
                    self.labyrinth.objects[i],
                    self.labyrinth.object_positions[i])
            )

    def display(self):
        """ This method displays the labyrinth in graphical mode """
        pygame.display.set_caption("Labyrinth Game")
        self.window_surface = pygame.display.set_mode(
            constants.window_resolution, pygame.RESIZABLE
        )
        self.text_display()

        while self.game_is_running:
            self.move()
            self.object_display()

    def manage_and_display_objects(self):
        """ This méthod manages the objects pick up """
        for ob in self.objects:
            if self.macgyver.position == ob.position:
                ob.is_pick_up = True
            if not ob.is_pick_up:
                self.window_surface.blit(
                    ob.load_image, [ob.position.x * 40, ob.position.y * 40]
                )

    def is_all_objects_is_pick_up(self):
        """ This method checks the objects are pick up """
        for object in self.objects:
            if not object.is_pick_up:
                return False
        return True

    def go_to_the_guardian(self):
        """ This method manages the end of the game """
        if (
            self.macgyver.position == self.labyrinth.arrival
            and self.is_all_objects_is_pick_up() is True
        ):
            self.window_surface.blit(self.game_win, self.rectTexte)
            pygame.time.wait(5000)
            self.game_is_running = False
        if (
            self.macgyver.position == self.labyrinth.arrival
            and self.is_all_objects_is_pick_up() is False
        ):
            self.window_surface.blit(self.game_over, self.rectTexte)
            pygame.time.wait(5000)
            self.game_is_running = False

    def text_display(self):
        """ This methdo display the text at the end of the game """
        rectScreen = self.window_surface.get_rect()

        police = pygame.font.Font("resources/LED Dot-Matrix.ttf", 60)
        self.game_over = police.render(
            "Game Over", True, pygame.Color("#DC143C")
            )
        self.rectTexte = self.game_over.get_rect()
        self.rectTexte.center = rectScreen.center

        self.game_win = police.render("Win Win", True, pygame.Color("#00FF7F"))
        self.rectTexte = self.game_win.get_rect()
        self.rectTexte.center = rectScreen.center

    def move(self):
        """ This method moves Macgyver in the labyrinth """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.macgyver.position.go_down(self.labyrinth.streets)
                elif event.key == pygame.K_UP:
                    self.macgyver.position.go_up(self.labyrinth.streets)
                elif event.key == pygame.K_LEFT:
                    self.macgyver.position.go_left(self.labyrinth.streets)
                elif event.key == pygame.K_RIGHT:
                    self.macgyver.position.go_right(self.labyrinth.streets)

    def object_display(self):
        """ This method displays all objects in the labyrinth """
        self.window_surface.fill(constants.blank_color)
        # streets
        for street in self.labyrinth.streets:
            self.window_surface.blit(
                constants.streets, [street.x * 40, street.y * 40]
                )
        # walls
        for wall in self.labyrinth.walls:
            self.window_surface.blit(
                constants.walls, [wall.x * 40, wall.y * 40]
                )
        # departure
        self.window_surface.blit(
            constants.departure,
            [self.labyrinth.departure.x * 40, self.labyrinth.departure.y * 40],
        )
        # arrival
        self.window_surface.blit(
            constants.arrival,
            [self.labyrinth.arrival.x * 40, self.labyrinth.arrival.y * 40],
        )
        # macgyver
        self.window_surface.blit(
            constants.hero,
            [self.macgyver.position.x * 40, self.macgyver.position.y * 40],
        )
        # objects
        self.manage_and_display_objects()
        self.is_all_objects_is_pick_up()
        self.go_to_the_guardian()
        pygame.display.flip()

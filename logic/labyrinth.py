import random

import pygame
from logic.position import Position


class Labyrinth:
    """This class define the labyrinth model"""

    def __init__(self):
        """This method is the constructor of the Labyrinth class"""
        self.streets = []
        self.walls = []
        self.width = None
        self.heigth = None
        self.departure = None
        self.arrival = None
        self.macgyver = None
        self.object_positions = None
        self.objects = []

    def load_labyrinth_from_file(self, file_name):
        """-This method allows to:
        -Read labyrinth file
        -Determine labyrinth height and width
        -Determine walls and streets in the labyrinth"""

        with open("resources/labyrinth.txt", "r") as my_file:
            my_labyrinth = my_file.readlines()

            # Determination of the street and wall of the labyrinth
            for j, ligne in enumerate(my_labyrinth):
                for i, caracter in enumerate(ligne.strip()):
                    if caracter == ".":
                        self.streets.append(Position(i, j))
                    elif caracter == "#":
                        self.walls.append(Position(i, j))
                    elif caracter == "D":
                        self.departure = Position(i, j)
                        self.streets.append(Position(i, j))
                    elif caracter == "A":
                        self.arrival = Position(i, j)
                        self.streets.append(Position(i, j))

            # Determination of the heigh and width of the labyrinth
            self.heigth = len(my_labyrinth)
            self.width = len(my_labyrinth[0].strip())

            self.object_positions = random.sample(
                set(self.streets) - {self.departure, self.arrival}, k=3
            )
            self.objects.append(self.create_object())
            self.objects = [objet for image in self.objects for objet in image]

    def is_streets(self, position):
        """This methode return true if the position is a street"""
        if position in self.streets:
            return True
        return False

    def is_walls(self, position):
        """This method return true if the position is a wall"""
        if position in self.walls:
            return True
        return False

    def create_object(self):
        """ This method create the needle, ether and seringue objects """
        self.needle = pygame.image.load("stage/needle.png")
        self.ether = pygame.image.load("stage/ether.png")
        self.seringue = pygame.image.load("stage/seringue.png")
        return self.needle, self.ether, self.seringue

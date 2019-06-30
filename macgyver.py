class MacGyver:
    """This class define the position and the characteristic of the hero MacGyver"""


    def __init__(self, labyrinth):
        """This method is the constructor of the class MacGyver"""
        self.labyrinth = labyrinth
        self.position = self.labyrinth.departure
        self.labyrinth.macgyver = self


    def move(self, direction):
        """This method determine the different movements of MacGyver."""
        new_position = getattr(self.position, direction)()
        if self.labyrinth.is_streets(new_position):
            self.position = new_position




        

       
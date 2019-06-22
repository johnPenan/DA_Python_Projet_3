class MacGyver:
    """This class define the position and the characteristic of the hero MacGyver"""


    def __init__(self, labyrinth):
        """This method is the constructor of the class MacGyver"""
        self.position = None
        self.labyrinth = labyrinth
        self.labyrinth.macgyver = self


    def move_macgyver(self, direction):
        """This method determine the different movements of MacGyver."""
        new_position = getattr(self.position, direction)
        if new_position in self.labyrinth.streets:
            self.position = new_position

        

       
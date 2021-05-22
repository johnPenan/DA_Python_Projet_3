class MacGyver:
    """This class define the position and the characteristic of the hero MacGyver
    """

    def __init__(self, labyrinth):
        """This method is the constructor of the class MacGyver"""
        self.labyrinth = labyrinth
        self.position = self.labyrinth.departure
        self.labyrinth.macgyver = self
        self.items = []

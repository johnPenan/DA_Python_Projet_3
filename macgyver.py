class MacGyver:
    """This class define the position and the characteristic of the hero MacGyver"""


    def __init__(self, labyrinth):
        """This method is the constructor of the class MacGyver"""
        self.labyrinth = labyrinth
        self.position = self.labyrinth.departure
        self.labyrinth.macgyver = self
        self.items = []
        


    def move(self, direction):
        """This method determine the different movements of MacGyver."""
        new_position = getattr(self.position, direction)()
        if self.labyrinth.is_streets(new_position) and new_position not in self.labyrinth.object_positions:
            self.position = new_position

        elif new_position in self.labyrinth.object_positions:
            if self.labyrinth.object_positions[0] == "n":
                self.items = [self.labyrinth.object_positions[0]]
                new_position = self.items
            elif self.labyrinth.object_positions[1] == "t":
                self.items = [self.labyrinth.object_positions[1]]
                new_position = self.items
            elif self.labyrinth.object_positions[0] == "e":
                self.items = [self.labyrinth.object_positions[2]]
                new_position = self.items

    # for i in self.labyrinth.object_positions:
    #     if new_position in self.labyrinth.object_positions:
    #         self.items = [self.labyrinth.object_positions[i]]
    #         i += 1





    

    



            




        

       
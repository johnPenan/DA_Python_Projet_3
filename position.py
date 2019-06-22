class Position:
    """This class define the different position of Macgyver"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

   
    def go_up(self):
        """This method define the up direction of MacGyver"""
        return Position(self.x-1, self.y)

    def go_down(self):
        """This method define the down direction of MacGyver"""
        return Position(self.x+1, self.y)

    def go_left(self):
        """This method define the left direction of MacGyver"""
        return Position(self.x, self.y-1)

    def go_right(self):
        """This method define the right direction of MacGyver"""
        return Position(self.x, self.y+1)

    def __repr__(self):
        return str((self.x, self.y))






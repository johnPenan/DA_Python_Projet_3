class Position:
    """This class define the different position of Macgyver"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

   
    def go_up(self, streets):
        """This method define the up direction of MacGyver"""
        #return Position(self.x-1, self.y)
        self.y -=1
        if(self not in streets):
            self.y += 1

    def go_down(self, streets):
        """This method define the down direction of MacGyver"""
        #return Position(self.x+1, self.y)
        self.y +=1
        if(self not in streets):
            self.y -= 1

    def go_left(self, streets):
        """This method define the left direction of MacGyver"""
        #return Position(self.x, self.y-1)
        self.x -=1
        if(self not in streets):
            self.x +=1

    def go_right(self, streets):
        """This method define the right direction of MacGyver"""
        """return Position(self.x, self.y+1)"""
        self.x +=1
        if(self not in streets):
            self.x -=1

    def __repr__(self):
        return str((self.x, self.y))


    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

    def __hash__(self):
        return hash((self.x, self.y))

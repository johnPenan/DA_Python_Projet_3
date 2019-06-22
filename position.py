class Position:
    """This class define the different position of Macgyver"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

   
    def _go_up(self):
        """This method define the up direction of MacGyver"""
        return Position(self._x-1, self._y)

    def _go_down(self):
        """This method define the down direction of MacGyver"""
        return Position(self._x+1, self._y)

    def _go_left(self):
        """This method define the left direction of MacGyver"""
        return Position(self._x, self._y-1)

    def _go_right(self):
        """This method define the right direction of MacGyver"""
        return Position(self._x, self._y+1)

    def __repr__(self):
        return str((self._x, self._y))



p = Position(0, 0)

print(p._go_down())





class Position:
    """This class the different position of Macgyver"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

   
    def _get_up(self):
        return Position(self._x-1, self._y)

    def _get_down(self):
        return Position(self._x+1, self._y)

    def _get_left(self):
        return Position(self._x, self._y-1)

    def _get_right(self):
        return Position(self._x, self._y+1)

    def __repr__(self):
        return str((self._x, self._y))




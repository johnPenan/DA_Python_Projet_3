class Object:
    """ This class manage the objects created in the labyrinth """
    def __init__(self, load_image, position):
        """ This method is the constructor of Object class """
        self.load_image = load_image
        self.position = position
        self.is_pick_up = False

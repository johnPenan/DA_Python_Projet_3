class Labyrinth:
    """This class define the labyrinth model"""

    def __init__(self):
        """ This method is the constructor of the class Labyrinth"""
        self.streets = []
        self.walls = []
        self.width = None
        self.heigth = None
        self.departure = None
        self.arrival = None
        self.macgyver = None
        self.position = None


    def load_labyrinth_from_file(self, file_name):
        """-This method allows to:
           -Read labyrinth file
           -Determine labyrinth height and width
           -Determine walls and streets in the labyrinth"""

        with open("labyrinth.txt", "r") as my_file:
            my_labyrinth = my_file.readlines()

            #Determination of the street and wall of the labyrinth
            for i, ligne in enumerate(my_labyrinth):
                for j, caracter in enumerate(ligne.strip()):
                    if caracter == '.':
                        self.streets.append((i,j))
                    elif caracter == '#':
                        self.walls.append((i,j))
                    elif caracter == 'D':
                        self.departure = (i,j)
                    elif caracter == 'A':
                        self.arrival = (i,j)   
            
            # Determination of the heigh and width of the labyrinth
                self.heigth = len(my_labyrinth)
                self.width = len(my_labyrinth[0].strip())
              
     def is_streets(self, position):
        """This methode return true if the position is a street"""
        if self.position in labyrinth.streets:
            self.macgyver = new_position
            return self.macgyver

    def is_walls(self, position):
        """This method return true if the position is a wall"""
        if self.position in labyrinth.walls:
            return self.macgyver



    def display_labyrinth(labyrinth):
        """This method display the labyrinth"""
        for i in range(labyrinth.heigth):
            for j in range(labyrinth.width):
                if Position(i, j) == labyrinth.macgyver.position:
                    print("H")
                elif Position(i, j) in labyrinth.streets:
                    print(Position(i, j))
                elif Position(i, j) in labyrinth.walls:
                    print(Position(i, j))

   





lab = Labyrinth()
macgyver = MacGyver(lab)

macgyver.display_labyrinth("labyrinth.txt")


       



 




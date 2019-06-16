
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

        return {
            "streets": self.streets,
            "walls": self.walls,
            "width": self.width,
            "heigth": self.heigth,
            "departure": self.departure,
            "arrival": self.arrival
        }



 
#Creation of Labyrinth object and loading labyrinth.txt file
labyrinth = Labyrinth()

print(labyrinth.load_labyrinth_from_file("labyrinth.txt"))



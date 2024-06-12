class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Animal sound"
    
class Mammal(Animal):

    def __init__(self, name, species):
        super().__init__(name, species)

    def give_birth(self):
        return(f"{self.name} the {self.species} has given birth")

class Bird(Animal):

    def __init__(self, name, species, wingspan):
        self.wingspan = wingspan
        super().__init__(name, species)

class Reptile(Animal):

    def __init__(self, name, species):
        super().__init__(name, species)

    def bask_in_sun(self):
        return (f"{self.name} the {self.species} is basking in the sun")

class Human(Mammal):

    def __init__(self, name, species):
        super().__init__(name, species)

class Kong(Mammal):

    def __init__(self, name, species):
        super().__init__(name, species)

    def __str__(self):
        print(f"{self.name} is the king of the animals!")

class Primate(Mammal):

    def __init__(self, name, species):
        super().__init__(name, species)

    def climb_trees(self):
        return(f"{self.name} the {self.species} is climbing trees")

class Marsupial(Mammal):

    def __init__(self, name, species):
        super().__init__(name, species)

    def carry_baby(self):
        return(f"{self.name} the {self.species} is carrying its baby")

class Aviary:
    birds_list = []

    def __init__(self, birds=[]):
        self.birds = birds
        Aviary.birds_list.append(self.birds)
    


class ReptileEnclosure():
    reptiles_list = []

    def __init__(self, reptiles=[]):
        self.reptiles = reptiles
        ReptileEnclosure.reptiles_list.extend(self.reptiles)


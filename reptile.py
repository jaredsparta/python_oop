from animal import Animal

class Reptile(Animal):
    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chambers = 3
        self.amniotic_eggs = True


    def seek_heat(self):
        return "Find the sun"


    def hunt(self):
        return "Find a prey"


    def use_venom(self):
        return "Bite"


    def attract_mate_through_scent(self):
        return "Find a mate through"


# # Creates a reptile object
# reptile = Reptile()
# 
# # These are methods from the Parent class, Animal
# print(reptile.breathe())
# print(reptile.move())
# 
# # These are methods from the Reptile class
# print(reptile.hunt())
# print(reptile.seek_heat())

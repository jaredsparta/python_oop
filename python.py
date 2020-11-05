from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.size = "Large"
        self.two_lungs = True
        self.venom = False

    
    def digest_large_prey(self):
        return "Digest prey"


    def constrict(self):
        return "Constricts prey"


    def climb(self):
        return "Does its best to climb"

    
    def shed_skin(self):
        return "Sheds its skin"


python = Python()

# # Methods and attributes from Python class
# print("From Python:")
# print(python.shed_skin())
# print(python.size)
# 
# # From Snake class
# print("\nFrom Snake:")
# print(python.limbs)
# print(python.use_tongue_to_smell())
# 
# 
# # From Reptile class
# print("\nFrom Reptile:")
# print(python.use_venom())
# print(python.tetrapod)
# 
# # From Animal class
# print("\nFrom Animal:")
# print(python.alive)
# print(python.procreate())
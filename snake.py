from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    
    def use_tongue_to_smell(self):
        return "Uses its tongue to smell"


snake = Snake()

# # Methods from the reptile class
# print(snake.forked_tongue)
# print(snake.use_venom())
# 
# # Method from the Snake class
# print(snake.use_tongue_to_smell())
# 
# # This is from the Animal class
# print(snake.move())

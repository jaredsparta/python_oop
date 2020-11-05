class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.lungs = True
        self.eyes = True

    def breathe(self):
        return "Breathing keeps us alive"

    
    def move(self):
        return "*moves*"

    
    def eat(self):
        return "Yum yum"

    
    def procreate(self):
        return "Find a mate"

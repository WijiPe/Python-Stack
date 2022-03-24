from classes.charactor import Character

class Pirate (Character):

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        self.strength += 2

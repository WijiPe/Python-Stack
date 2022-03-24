from classes.charactor import Character

class Ninja (Character):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        self.speed += 2
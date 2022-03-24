from Dojo_Ninja import Ninja

class Pet:
    def __init__(self, name , type , tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def __str__(self) -> str:
            return f"{self.name} is a {self.type}, she loves to {self.tricks} the sofa. And she is {self.special} and {self.behavior}."

    def sleep(self):
        self.energy += 25
        print (self)
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print (self)
        return self

    def play(self):
        self.energy += 5
        self.health += 10
        print (self)
        return self

    def noise(self):
        print("meawwwwww")
        return self

class Bad_pet(Pet):
    def __init__(self, name, type, tricks, health, energy, special):
        super().__init__(name, type, tricks, health, energy)
        self.behavior = "stubborn"
        self.special = special
    def pet_lazyPet(self):
        super().sleep()
        print("lazy pet")
        return self

class Good_pet(Pet):
    def __init__(self, name, type, tricks, health, energy, special):
        super().__init__(name, type, tricks, health, energy)
        self.behavior = "snuggle"
        self.special = special
    def pet_obeyPet(self):
        super().sleep()
        print("good listener")
        return self

taco = Good_pet("Taco", "cat", "smile" ,100,100, "hard worker")
noodle = Bad_pet("Noodle", "cat", "scratch" ,100,100, "lazy")
ninja1 = Ninja("Jojo", "Lala", "catnip biskit", "salmon", taco)



print(ninja1)
print(noodle)
print(taco)
noodle.pet_lazyPet()

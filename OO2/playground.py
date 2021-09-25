class Pet:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def hello(self):
        print(self.name)


class Cat(Pet):
    pass


myCat = Cat("Mietz", 8)
myCat.age = 12
print(myCat.name, myCat.age)

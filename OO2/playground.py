class Pet:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def hello(self):
        print(self.name)


class Cat(Pet):
    def speak(cls):
        return True


myCat = Cat("Mietz", 8)
print(myCat.name, myCat.age)

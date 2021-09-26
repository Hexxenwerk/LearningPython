class Person:
    def __init__(self, name: str):
        self.name = name

    def talk(self, say: str):
        print(f"{self.name} says {say}")


p1 = Person("Suzi")
p1.talk("Hello")

import random


def dice() -> tuple:
    return random.randint(1, 6), random.randint(1, 6)


print(dice())

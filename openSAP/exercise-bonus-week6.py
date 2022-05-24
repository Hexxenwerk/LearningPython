from math import pi
from random import random

my_pi = len([True for _ in range(10000) if random() ** 2 + random() ** 2 < 1]) / 10000 * 4

print(f'Calculated value of π: {my_pi}')

print(f'Value of π from math library: {pi}')
print(f'Difference: {abs(pi - my_pi)}')

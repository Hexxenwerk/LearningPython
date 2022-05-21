import math
import random

points_in_square = [(random.random(), random.random()) for _ in range(10000)]
points_in_circle = [(x, y) for x, y in points_in_square if x ** 2 + y ** 2 < 1]
my_pi = len(points_in_circle) / len(points_in_square) * 4

print(f'Calculated value of π: {my_pi}')

print(f'Value of π from math library: {math.pi}')
print(f'Difference: {abs(math.pi - my_pi)}')

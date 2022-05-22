import math
import random

points_in_square = [(random.random(), random.random()) for _ in range(10000)]
count_in_circle = len([(x, y) for x, y in points_in_square if x * x + y * y < 1])
my_pi = count_in_circle / len(points_in_square) * 4

print(f'Calculated value of π: {my_pi}')

print(f'Value of π from math library: {math.pi}')
print(f'Difference: {abs(math.pi - my_pi)}')

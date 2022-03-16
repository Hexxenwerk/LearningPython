""" Type conversion / Type casting """
"""
int()
float()
str()
"""

x = "10"
print(x, type(x))

x = int(x)
print(x, type(x))

x = float(x)
print(x, type(x))

x = str(x)
print(x, type(x))

###############################
# Example 1:

num1 = input('Num1: ')  # "10"
num2 = input('Num2: ')  # "5"

# Conversion
num1 = int(num1)  # 10
num2 = int(num2)  # 5
print(num1 + num2)  # 10 + 5 = 105

###############################
# Example 2 (incl. Conversion):

num1 = int(input('Num1: '))  # 10
num2 = int(input('Num2: '))  # 5

print(num1 + num2)  # 10 + 5 = 105

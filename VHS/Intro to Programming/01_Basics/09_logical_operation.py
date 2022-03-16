print(10 > 3)
print(10 < 3)
print(10 >= 3)
print(10 <= 3)

# Zuweisen
x, y = 10, 20

# Vergleich
print(x == y)  # ob x gleich y ist
print(x != y)  # ob x ungleich y ist

######################################
# Multi-Condition: "and" "or"
x, y = 10, 20
print('1:', x == 10 and y == 20)  # True
print('2:', x == 10 or y == 20)  # True
print('3:', x == 10 or y != 18)  # True
print('4:', x != 16 and y != 8)  # True

######################################
# not : True -> False , False -> True
anwesend = True
print(not anwesend)

######################################
# in
course_name = "Python Programming"
print("Python" in course_name)  # True
print("Java" in course_name)  # False

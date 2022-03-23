# Functions
numbers = [4, 7, 2, 8, 3, 9, 4]
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(len(numbers))

# Creates a new list w/o changing original list
new_list = sorted(numbers)  # aufsteigend
print(numbers)
print(new_list)
new_list = sorted(numbers, reverse=True)
print(new_list)

###############################################
# Methods
print(numbers.count(4))
numbers.sort()
print(numbers)

###############################################
# in -> check if specific value exists
print(4 in numbers)
print(5 in numbers)

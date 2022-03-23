# Empty List
teilnehmer_liste = []
print(teilnehmer_liste, type(teilnehmer_liste))

# Only numbers
numbers = [1, 2, 3, 4, 5]
print(numbers, type(numbers))

# Only characters
characters = ["A", "B", "C"]
print(characters, type(characters))

# Mixed data types within one list
mixed_data = ["Thomas", 45, 36.9, True, teilnehmer_liste, numbers, characters]
print(mixed_data, type(mixed_data))

zeros = [0] * 30
print(zeros)

# Combined list
combined_list = mixed_data + characters
print(combined_list)

matrix = [[1, 2], [3, 4]]
print(matrix)

# Conversion list()
course_name = 'Python'
print(list(course_name))  # ['P', 'y', 't', 'h', 'o', 'n']
print(list(range(10)))

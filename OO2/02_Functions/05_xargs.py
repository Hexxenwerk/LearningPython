def show_numbers_1(n1: int, n2: int, n3=0):
    print(n1 + n2 + n3)


def show_numbers_2(*numbers):
    print(numbers, type(numbers))
    print(sum(numbers))


show_numbers_1(1, 4, 9)
show_numbers_2(3, 5, 8)

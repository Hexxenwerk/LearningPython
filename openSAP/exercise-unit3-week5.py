def is_even(number):
    return not bool(number % 2)


for n in range(100):
    if is_even(n):
        print(f'{n} is even')
    else:
        print(f'{n} is not even')

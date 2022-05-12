def get_number():
    while True:
        try:
            return int(input('Enter an number: '))
        except ValueError:
            print('You must enter a number.')


def fac(number: int) -> int:
    factor = 1
    for n in range(number, 0, -1):
        factor *= n
    return factor


def main():
    number = get_number()
    factor = fac(number)
    print(factor)


if __name__ == '__main__':
    main()

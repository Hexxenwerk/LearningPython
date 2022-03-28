# X-argument (beliebige Anzahl von werten)

def addieren_1(num1: int, num2: int, num3: int):
    return sum([num1, num2, num3])


def addieren_2(*args):
    return sum(args)


def main():
    print(addieren_1(3, 4, 0))
    print(addieren_2(3, 4, 0, 5, 7, 1))


if __name__ == '__main__':
    main()

def funkt_1(monat: str):
    [print(f'{n + 1}: {x}') for n, x in enumerate(monat[0:5]) if monat == "Dezember"]


def funkt_2(monat: str):
    for x in enumerate(monat):
        print(f'{x[0] + 1}: {x[1]}')


def funkt_3(monat: str):
    counter = 0
    for x in monat:
        print(f'{counter}: {x}')
        counter += 1


def funkt_4(monat: str):
    for counter, x in enumerate(monat):
        print(f'{counter}: {x}')


def main():
    funkt_1("Dezember")
    funkt_2("November")
    funkt_3("September")
    funkt_4("Oktober")


if __name__ == '__main__':
    main()

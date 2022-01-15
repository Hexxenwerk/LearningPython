from typing import List, Union


def funkt_1(monat: str):
    [print(f'{n + 1}: {x}') for n, x in enumerate(monat)]


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


def funkt_5(monat: str):
    for i in range(len(monat)):
        print(f'{i}: {monat[i]}')


def funkt_6(monat_1, monat_2: str) -> List[Union[str, str]]:
    result = {}
    for x in monat_1:
        if x in monat_2:
            result[x] = True
    return sorted(result.keys())


def funkt_7(monat_1, monat_2: str) -> List[Union[str, str]]:
    result = {}
    for x in monat_1:
        if x not in monat_2:
            result[x] = True
    for x in monat_2:
        if x not in monat_1:
            result[x] = True
        return sorted(result.keys())


def main():
    funkt_1("Dezember")
    funkt_2("November")
    funkt_3("September")
    funkt_4("Oktober")
    funkt_5("Januar")
    print(funkt_6("Dezember", "November"))
    print(funkt_7("Dezember", "Januar"))


if __name__ == '__main__':
    main()

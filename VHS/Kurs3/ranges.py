def abkuerzung_fuer_schleife(zahl: int):
    [print(n) for n in range(1, zahl + 1)]


def buchstaben_ausgeben(wort: str):
    [print(x) for x in wort]


def monat_ausgeben(monat: str):
    [print(x) for x in monat]


def main():
    [print(n) for n in range(0, 10)]
    [print(n) for n in range(1, 11)]
    [print(n) for n in range(10, 21)]
    [print(n) for n in range(10, 21, 2)]
    [print(n) for n in range(20, 7, -3)]
    [print(x) for x in "January"]
    abkuerzung_fuer_schleife(8)
    buchstaben_ausgeben("Januar")
    monat_ausgeben("Dezember")


if __name__ == '__main__':
    main()

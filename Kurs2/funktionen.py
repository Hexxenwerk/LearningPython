def funkt_neu(monat):
    [print(f'{n}: {x}') for n, x in enumerate(monat[0:2]) if monat == "Dezember"]


def main():
    funkt_neu("Dezember")


if __name__ == '__main__':
    main()

def getintput() -> int:
    try:
        zahl: int = int(input("> "))
        return zahl
    except ValueError:
        print("Die Eingabe muss numerisch sein.")
        return getintput()


def getnumbers() -> list:
    numbers: list = []
    while True:
        zahl: int = getintput()
        if not zahl:
            return numbers
        numbers.append(zahl)


def get_numbers_struct(numbers) -> dict:
    numbers_struct: dict = {
        "positiv": [],
        "negativ": [],
        "sum_all": 0,
        "sum_pos": 0,
        "sum_neg": 0
    }
    for i in numbers:
        if i > 0:
            numbers_struct["positiv"].append(i)
            numbers_struct["sum_pos"] += i
        else:
            numbers_struct["negativ"].append(i)
            numbers_struct["sum_neg"] += i

    numbers_struct["sum_all"] = sum(numbers)

    return numbers_struct


def main():
    print("Gib eine Zahl pro Zeile ein. Gib zum Abschließen eine 0 ein.")
    numbers: list = getnumbers()
    numbers_struct: dict = get_numbers_struct(numbers)
    if not numbers:
        print("Die Liste ist leer. Keine Operation möglich.")
        exit(0)
    print("Alle Zahlen sind:", numbers)
    print("Alle positiven Zahlen sind:", numbers_struct["positiv"])
    print("Alle negativen Zahlen sind:", numbers_struct["negativ"])
    print("Die Summe aller Zahlen ist:", numbers_struct["sum_all"])
    print("Die Summe der positiven Zahlen ist:", numbers_struct["sum_pos"])
    print("Die Summe der negativen Zahlen ist:", numbers_struct["sum_neg"])


exit(main())

from datetime import datetime

from Kurs2.bank import person
from Kurs2.bank.bank import Bank
from Kurs2.bank.konto import Konto


def main():
    naspa = Bank(name="Nassauische Sparkasse", firmensitz="Wiesbaden", land="DE", bic="NASSDE55XXX", blz=51050015)
    person_1 = person.Person(person.NewAutomated("Barney", "Geröll", datetime(1988, 12, 22), "GeHeiM", True, "m"))
    person_2 = person.Person(person.NewInteractive())
    konto_1 = Konto(besitzer=person_1, bank=naspa)
    konto_2 = Konto(besitzer=person_2, bank=naspa)
    print(person_1)
    print(person_2)
    print(konto_1)
    print(konto_2)
    konto_1.einzahlen()
    print(konto_1)


if __name__ == '__main__':
    main()

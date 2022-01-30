from datetime import datetime

from VHS.Kurs3.bank import person
from VHS.Kurs3.bank.bank import Bank
from VHS.Kurs3.bank.konto import Konto


def main():
    naspa = Bank(name="Nassauische Sparkasse", firmensitz="Wiesbaden", land="DE", bic="NASSDE55XXX", blz=51050015)
    targo = Bank(name="TARGOBANK AG", firmensitz="Düsseldorf", land="DE", bic="CMCIDEDDXXX", blz=30020900)

    person_1 = person.Person("Barney", "Geröllheimer", datetime(1988, 12, 22), "GeHeiM", True, "m")
    person_2 = person.Person.new()

    konto_1 = Konto(besitzer=person_1, bank=naspa)
    konto_2 = Konto(besitzer=person_2, bank=targo, kontostand=100)

    print(naspa)
    print(targo)

    print(person_1)
    print(person_2)

    print(konto_1)
    print(konto_2)

    konto_1.einzahlen()
    konto_2.einzahlen(betrag=1200.55)

    print(konto_1)
    print(konto_2)

    print(f'Anzahl Konten: {len(Konto.anzahl_konten)}')

    del konto_1, konto_2, person_1, person_2

    print(f'Anzahl Konten: {len(Konto.anzahl_konten)}')


if __name__ == '__main__':
    main()

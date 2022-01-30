from datetime import datetime

from VHS.Kurs4.store.artikel.kleidung import Pullover, Hose
from VHS.Kurs4.store.interaktion import kunden
from VHS.Kurs4.store.personen import Gender
from VHS.Kurs4.store.personen.kunden import Kunde, Kundenliste


def main():
    pullover_1 = Pullover('blau', 15.5, 'XL')
    pullover_2 = Pullover('grün', 25.0, 'SL')
    hose_1 = Hose('schwarz', 75.0, 34)
    hose_2 = Hose('pink', 95.5, 33)

    kunde_1 = Kunde("Fred", "Feuerstein", geburtsdatum=datetime(1962, 12, 31), geschlecht=Gender("m"))
    kunde_2 = Kunde("Wilma", "Feuerstein", geburtsdatum=datetime(1963, 10, 12), geschlecht=Gender("w"))
    kunde_3 = Kunde("Betty", "Geröllheimer", geburtsdatum=datetime(1966, 11, 11), geschlecht=Gender("w"))

    kundenliste = Kundenliste.new()
    kundenliste.add(kunde_1, kunde_2, kunde_3)
    print("Ausgabe der Bestandskundenliste:")
    print(kundenliste.list())

    kunde_1.einkauf([pullover_1, hose_1, hose_2])
    kunde_2.einkauf([pullover_1, pullover_2, hose_2])
    print(f'{kunde_1.vorname} {kunde_1.nachname} hat einen Gesamtumsatz in Höhe von € {kunde_1.gesamtumsatz}')

    kunde_1.begruessung()

    kunden.neu(kundenliste)
    kundenliste.list(output=True)

    print(f'Abschlussrechung - Gesamtumsatz aller Kunden: {kundenliste.gesamtumsatz()}')


if __name__ == '__main__':
    main()

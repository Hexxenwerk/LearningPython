from VHS.Kurs4.store.artikel.kleidung import Pullover, Hose
from VHS.Kurs4.store.interaktion import kunden
from VHS.Kurs4.store.personen.kunden import Kunde, Kundenliste


def main():
    pullover_1 = Pullover('blau', 15.0, 'XL')
    hose_1 = Hose('schwarz', 75.0, 34)
    hose_2 = Hose('pink', 95.5, 33)

    kunde_1 = Kunde(vorname="Fred", nachname="Feuerstein", geschlecht="männlich")
    kunde_2 = Kunde(vorname="Wilma", nachname="Feuerstein", geschlecht="weiblich")
    kunde_3 = Kunde(vorname="Betty", nachname="Geröllheimer", geschlecht="weiblich")

    kundenliste = Kundenliste.new()
    kundenliste.add(kunde_1, kunde_2, kunde_3)
    print("Ausgabe der Bestandskundenliste:")
    kundenliste.list()

    kunde_1.einkauf([pullover_1, hose_1, hose_2])
    print(f'{kunde_1.vorname} {kunde_1.nachname} hat einen Gesamtumsatz in Höhe von € {kunde_1.gesamtumsatz}')

    kunde_1.begruessung()

    kunden.neu(kundenliste)


if __name__ == '__main__':
    main()

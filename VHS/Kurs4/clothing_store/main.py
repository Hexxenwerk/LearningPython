from VHS.Kurs4.clothing_store.artikel.kleidung import Pullover
from VHS.Kurs4.clothing_store.personen.kunden import Kunde, Kundenliste


def main():
    pullover_1 = Pullover('blau', 15.0, 'XL')
    print(pullover_1)

    kunde_1 = Kunde(vorname="Fred", nachname="Feuerstein", geschlecht="male")
    kunde_2 = Kunde(vorname="Betty", nachname="Geröllheimer", geschlecht="female")
    kundenliste = Kundenliste.new()
    kundenliste.add(kunde_1)
    kundenliste.add(kunde_2)
    kundenliste.list()
    kundenliste.remove(kunde_1)
    kundenliste.list()


if __name__ == '__main__':
    main()

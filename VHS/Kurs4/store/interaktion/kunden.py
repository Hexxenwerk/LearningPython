from VHS.Kurs4.store.personen import Gender
from VHS.Kurs4.store.personen.kunden import Kunde, Kundenliste


def neu(kundenliste: Kundenliste):
    print('Wilkommen in unserem Geschäft. Wir möchten sie als Neukunden anlegen.')
    try:
        vorname, nachname = input('Wir lautet ihr Vor- und Zuname? ').split(maxsplit=1)
        geschlecht = Gender(input('Sind sie männlich oder weiblich? [m/w] '))
    except KeyboardInterrupt:
        print('Das Programm wurde vom Benutzer abgebrochen')
    else:
        kundenliste.add(Kunde(vorname, nachname, geschlecht))

    return kundenliste.last_added()

from datetime import datetime

from VHS.Kurs4.store.personen import Gender
from VHS.Kurs4.store.personen.kunden import Kunde, Kundenliste


def neu(kundenliste: Kundenliste):
    print('Wilkommen in unserem Geschäft. Wir möchten sie als Neukunden anlegen.')
    try:
        vorname, nachname = input('Wir lautet ihr Vor- und Zuname? ').split(maxsplit=1)
        geschlecht = Gender(input('Sind sie männlich oder weiblich? [m/w] '))
        jahr, monat, tag = [int(n) for n in input('Wie lautet ihr Geburtsdatum? [YYYY MM DD] ').split()]
        geburtsdatum = datetime(jahr, monat, tag)
    except KeyboardInterrupt:
        print('Das Programm wurde vom Benutzer abgebrochen')
    except ValueError:
        print('Die Datumseingabe muss numerisch und durch Leerzeichen getrennt sein')
    else:
        kundenliste.add(Kunde(vorname, nachname, geburtsdatum, geschlecht))

    return kundenliste.last_added()

from datetime import datetime

from VHS.Kurs4.people.mensch import Person, Counter


def main():
    lfd_nummer: Counter = Counter()
    personen: dict = {
        'adam': Person(ledig=True, wohnort='Hamburg', gewicht=74.5, vorname='Adam', nachname='Bibel',
                       geschlecht='m', geburtsdatum=datetime(1973, 12, 12), nummer=lfd_nummer),
        'eva': Person(ledig=True, wohnort='Hamburg', gewicht=58.7, vorname='Eva', nachname='Friedrich',
                      geschlecht='w', geburtsdatum=datetime(1973, 10, 22), nummer=lfd_nummer),
    }

    for person in personen:
        alter: datetime = personen[person].geburtsdatum
        print(f'{personen[person].vorname:4} ist {(datetime.now() - alter).days} Tage alt.')
        print(personen[person])

    personen['adam'].geschlechtsumwandlung()
    print(f'Adam ist jetzt {personen["adam"].geschlecht} und heißt {personen["adam"].vorname}')

    # personen['adam'].ask_alter()
    print(f"{personen['adam'].vorname} ist tatsächlich {personen['adam'].get_alter()} Jahre alt")

    print(personen['adam'].heiratet(personen['eva']))
    print(personen['adam'].wird_beschrieben())
    print(personen['eva'].wird_beschrieben())


if __name__ == '__main__':
    main()

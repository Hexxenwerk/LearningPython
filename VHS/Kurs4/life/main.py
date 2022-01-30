import sys
from datetime import datetime
from os import getenv
from typing import List

import requests

from VHS.Kurs4.life.lebewesen import Counter, Frau, Mann, Mensch


def persons_print(personen) -> None:
    for person in personen:
        alter: datetime = personen[person].geburtsdatum
        print(f'{personen[person].vorname:4} ist {(datetime.now() - alter).days} Tage alt.')
        print(personen[person])


def persons_generate() -> List[Mensch]:
    personen_liste = []
    with open(getenv('HOME') + "/.config/name.parser/api_key", 'r') as reader:
        api_key = reader.readline().strip()
    response = requests.get(f'https://api.parser.name/?api_key={api_key}&endpoint=generate')
    if response.status_code != 200:
        print(f'Invalid status code {response.status_code}')
        sys.exit(1)
    data = response.json()
    personen_liste.append(
        Mensch(ledig=data['data'])
    )
    return personen_liste


def main():
    lfd_nummer: Counter = Counter()
    persons_generate()
    personen: dict = {
        'adam': Mann(ledig=True, wohnort='Hamburg', gewicht=74.5, vorname='Adam', nachname='Bibel',
                     geschlecht='m', geburtsdatum=datetime(1973, 12, 12), nummer=lfd_nummer),
        'eva': Frau(ledig=True, wohnort='Hamburg', gewicht=58.7, vorname='Eva', nachname='Friedrich',
                    geschlecht='w', geburtsdatum=datetime(1973, 10, 22), nummer=lfd_nummer),
    }

    persons_print(personen)

    personen['adam'].geschlechtsumwandlung()
    print(f'Adam ist jetzt {personen["adam"].geschlecht} und heißt {personen["adam"].vorname}')

    # personen['adam'].ask_alter()
    print(f"{personen['adam'].vorname} ist tatsächlich {personen['adam'].get_alter()} Jahre alt")

    print(personen['adam'].heiratet(personen['eva']))
    print(personen['adam'].wird_beschrieben())
    print(personen['eva'].wird_beschrieben())


if __name__ == '__main__':
    main()

import sys
from typing import Tuple


def suche_kleidungsstueck(kleider_liste, kunden_auswahl) -> int:
    try:
        return kleider_liste.index(kunden_auswahl)
    except ValueError:
        return -1


def kunden_abfrage(kleider_liste) -> (int, str):
    for i, kleidungstueck in enumerate(kleider_liste, start=1):
        print(f'{i}. {kleidungstueck}')
    eingabe = input('Welches Kleidungsstück möchen sie kaufen? ')
    try:
        return int(eingabe) - 1, ""
    except ValueError:
        return suche_kleidungsstueck(kleider_liste, eingabe), eingabe
    except KeyboardInterrupt:
        print(f'\nProgramm wurde vom Benutzer abgebrochen')
        sys.exit(0)


def main():
    kleider_liste: Tuple[str, str, str, str] = ('Pullover', 'Hose', 'Hemd', 'Handschuhe')
    kleider_preise: Tuple[float, float, float, float] = (12.0, 14.0, 35.0, 11.0)

    index, eingabe = kunden_abfrage(kleider_liste)
    if index == -1:
        print(f'Der Artikel "{eingabe}" wurde nicht gefunden.')
        sys.exit(0)

    print(f'Kleidungsstück Nr. {index + 1}: {kleider_liste[index]} kostet € {kleider_preise[index]}')


if __name__ == '__main__':
    main()

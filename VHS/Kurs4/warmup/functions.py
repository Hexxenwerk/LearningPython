import re
import sys
from typing import Tuple


def runs(limit: int) -> Tuple[int, int]:
    for durchlauf, counter in enumerate(range(limit, 0, -1), start=1):
        print(f'{durchlauf}. Durchlauf --------- {counter}')
        try:
            if re.match(r'ja?', input('Möchstest du abbrechen? [j/n] '), re.IGNORECASE):
                return durchlauf, counter
        except KeyboardInterrupt:
            print(f'\nProgramm wurde vom Benutzer abgebrochen')
            sys.exit(0)


def main():
    result = runs(5)
    print(f'Durchläufe: {result[0]} - Zähler: {result[1]}')


if __name__ == '__main__':
    main()

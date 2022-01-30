from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from gender import gender

from VHS.Kurs4.clothing_store.personen import Person


class Kunde(Person):
    kundennummer = 0

    def __init__(self, vorname: str, nachname: str, geschlecht: gender):
        super().__init__(vorname, nachname, geschlecht)
        self._gesamtumsatz = 0.0
        self._umsaetze: Dict[datetime: float]
        Kunde.kundennummer += 1


@dataclass()
class Kundenliste:
    _kundenliste: List[Kunde]

    @staticmethod
    def new():
        return Kundenliste([])

    def add(self, kunde: Kunde) -> None:
        try:
            self._kundenliste.index(kunde)
            print(f'Kunde existiert bereits in der Liste: {kunde}')
        except ValueError:
            self._kundenliste.append(kunde)

    def remove(self, kunde: Kunde) -> None:
        try:
            self._kundenliste.remove(kunde)
        except ValueError:
            print(f'Fehler: Kunde nicht in Liste: {kunde}')

    def list(self):
        for kunde in self._kundenliste:
            print(kunde)

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from gender import gender

from VHS.Kurs4.store.artikel import Artikel
from VHS.Kurs4.store.personen import Person


class Kunde(Person):
    kundennummer = 0

    def __init__(self, vorname: str, nachname: str, geschlecht: gender):
        super().__init__(vorname, nachname, geschlecht)
        self._gesamtumsatz = 0.0
        self._umsaetze: Dict[datetime: float] = {}
        Kunde.kundennummer += 1

    def begruessung(self):
        print(f'Willkommen zurück in unserem Geschäft {self.vorname}')

    def einkauf(self, artikel: List[Artikel]):
        self._gesamtumsatz += sum([a.preis for a in artikel])
        self._umsaetze[datetime.now()] = artikel

    @property
    def gesamtumsatz(self):
        return self._gesamtumsatz


@dataclass()
class Kundenliste:
    _kundenliste: List[Kunde]

    @staticmethod
    def new():
        return Kundenliste([])

    def add(self, *kunde: Kunde) -> None:
        for k in kunde:
            try:
                self._kundenliste.index(k)
                print(f'Kunde existiert bereits in der Liste: {k}')
            except ValueError:
                self._kundenliste.append(k)

    def remove(self, kunde: Kunde) -> None:
        try:
            self._kundenliste.remove(kunde)
        except ValueError:
            print(f'Fehler: Kunde nicht in Liste: {kunde}')

    def list(self):
        for kunde in self._kundenliste:
            print(kunde)

    def last_added(self):
        return self.list()[-1]

    def gesamtumsatz(self):
        return sum(list([kunde.gesamtumsatz() for kunde in self._kundenliste]))

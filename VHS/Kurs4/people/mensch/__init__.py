from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Counter:
    def __init__(self):
        self.number = None


@dataclass()
class Mensch:
    geschlecht: str
    geburtsdatum: datetime


@dataclass()
class Person(Mensch):
    ledig: bool
    wohnort: str
    gewicht: float
    vorname: str
    nachname: str
    nummer: Counter
    _genanntes_alter: int = 0

    def heiratet(self, partner):
        if self == partner:
            return f'{self.vorname} kann sicht nicht selbst heiraten.'
        if not self.ledig and partner.ledig:
            return f'Können nicht heiraten, da nicht beide ledig sind.'
        partner.nachname = "-".join([self.nachname, partner.nachname])
        self.nachname = partner.nachname
        self.ledig, partner.ledig = False, False
        return f'{self.vorname} und {partner.vorname} können heiraten'

    def ask_alter(self) -> None:
        while True:
            try:
                self._genanntes_alter = int(input(f'Wie alt ist {self.vorname}? '))
                break
            except ValueError:
                print('Eingabe muss numerisch sein.')

    def get_alter(self) -> int:
        if self.geschlecht == 'w':
            return self._genanntes_alter + 10
        return self._genanntes_alter

    def wird_beschrieben(self) -> str:
        return f'Es handelt sich um: {self.vorname}, {self.nachname}, {self.geburtsdatum.strftime("%d.%m.%Y")}, Ledig: {self.ledig}'

    def __str__(self):
        return f'{self.vorname} {self.nachname}, geboren: {self.geburtsdatum}'

    def geschlechtsumwandlung(self) -> None:
        if self.geschlecht == 'm':
            self.geschlecht = 'w'
            self.vorname = 'Carmen'
        elif self.geschlecht == 'w':
            self.geschlecht = 'm'
            self.vorname = 'Markus'

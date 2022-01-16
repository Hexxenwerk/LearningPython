from datetime import datetime
from getpass import getpass
from re import match
from typing import Union


class NewInteractive:
    def __init__(self):
        self.vorname = input("Vorname: ")
        self.nachname = input("Nachname: ")
        self.ledig = bool(match(r'ja?$', input('Verheiratet? ')))
        self.geschlecht = input('Sind sie männlich, weiblich oder divers? [m/w/d] ')
        self.geburtsdatum = self.__get_birthday()
        self.secret = getpass("Passwort für neuen Benutzer: ")

    @staticmethod
    def __get_birthday() -> datetime:
        eingabe = input("Geburtsdatum (DD.MM.YYYY): ")
        try:
            tag, monat, jahr = map(lambda x: int(x), eingabe.split('.', 2))
        except ValueError as err:
            print(f'Datumseingabe "{err}" ist ungültig')
        else:
            return datetime(jahr, monat, tag)


class NewAutomated:
    def __init__(self, vorname: str, nachname: str, geburtsdatum: datetime, secret: str, ledig: bool, geschlecht: str):
        self.geschlecht = geschlecht
        self.ledig = ledig
        self.geburtsdatum = geburtsdatum
        self.nachname = nachname
        self.vorname = vorname
        self.secret = secret


class Person:
    def __init__(self, new_person: Union[NewInteractive, NewAutomated]):
        self.geburtsdatum = new_person.geburtsdatum
        self.nachname = new_person.nachname
        self.vorname = new_person.vorname
        self.secret = new_person.secret
        self.ledig = new_person.ledig
        self.geschlecht = new_person.geschlecht

    def __str__(self) -> str:
        return f'{self.vorname}, {self.nachname}, {self.geburtsdatum}, {self.ledig}, {self.geschlecht}'

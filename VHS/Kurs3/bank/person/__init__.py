from datetime import datetime
from getpass import getpass
from re import match, IGNORECASE


class Person:
    @staticmethod
    def new():
        return Person(
            vorname=input("Vorname: "),
            nachname=input("Nachname: "),
            ledig=bool(match(r'ja?$', input('Verheiratet? [j/n] '), IGNORECASE)),
            geschlecht=input('Sind sie männlich, weiblich oder divers? [m/w/d] '),
            geburtsdatum=Person.__get_birthday(),
            secret=getpass("Passwort für neuen Benutzer: ")
        )

    @staticmethod
    def __get_birthday() -> datetime:
        eingabe = input("Geburtsdatum (DD.MM.YYYY): ")
        try:
            tag, monat, jahr = map(lambda x: int(x), eingabe.split('.', 2))
        except ValueError as err:
            print(f'Datumseingabe "{err}" ist ungültig')
        else:
            return datetime(jahr, monat, tag)

    def __init__(self, vorname: str, nachname: str, geburtsdatum: datetime, secret: str, ledig: bool, geschlecht: str):
        self.geschlecht = geschlecht
        self.ledig = ledig
        self.geburtsdatum = geburtsdatum
        self.nachname = nachname
        self.vorname = vorname
        self.secret = secret

    def __str__(self) -> str:
        return f'{self.vorname}, {self.nachname}, {self.geburtsdatum}, {self.ledig}, {self.geschlecht}'

    def __del__(self):
        print(f'Folgende Person wurde gelöscht:\n{self}')

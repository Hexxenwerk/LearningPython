from dataclasses import dataclass

from gender import gender


@dataclass()
class Person:
    vorname: str
    nachname: str
    geschlecht: gender

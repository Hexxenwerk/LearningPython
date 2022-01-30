import re
from dataclasses import dataclass


class Gender:
    def __init__(self, geschlecht: str):
        if re.match(r'w(?:eiblich)?$|f(?:rau)?$', geschlecht):
            self.geschlecht = 'w'
        elif re.match(r'm(?:ännlich)?$|m(?:aennlich)?$|f(?:rau)?$', geschlecht):
            self.geschlecht = 'm'
        elif re.match(r'd(?:divers)?$', geschlecht):
            self.geschlecht = 'd'
        else:
            print('Ungültige angabe des Geschlechts')


@dataclass()
class Person:
    vorname: str
    nachname: str
    geschlecht: Gender

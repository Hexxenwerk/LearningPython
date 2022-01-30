from dataclasses import dataclass
from typing import Union


@dataclass()
class Artikel:
    farbe: str
    preis: float
    groesse: Union[float, str]


@dataclass()
class Kleidung(Artikel):
    pass


@dataclass()
class Pullover(Kleidung):
    pass


@dataclass()
class Hemd(Kleidung):
    pass


@dataclass()
class Hose(Kleidung):
    pass


@dataclass()
class Schuhe(Kleidung):
    pass

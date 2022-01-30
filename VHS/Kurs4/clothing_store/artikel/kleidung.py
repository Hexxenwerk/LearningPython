from dataclasses import dataclass
from typing import Union


@dataclass()
class Artikel:
    pass


@dataclass(Artikel)
class Kleidung:
    farbe: str
    preis: float
    groesse: Union[float, str]


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

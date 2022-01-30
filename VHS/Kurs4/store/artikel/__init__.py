from dataclasses import dataclass
from typing import Union


@dataclass()
class Artikel:
    farbe: str
    preis: float
    groesse: Union[float, str]

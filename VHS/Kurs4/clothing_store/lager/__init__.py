import uuid
from dataclasses import dataclass
from typing import Union

from VHS.Kurs4.clothing_store.artikel.kleidung import Kleidung


@dataclass()
class Lager:
    artikel: Union[Kleidung]
    bestand: int = 100
    _artikelnummer = uuid.uuid4()
    _mindestbestand = 10

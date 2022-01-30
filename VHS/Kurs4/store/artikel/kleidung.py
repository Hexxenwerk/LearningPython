from dataclasses import dataclass

from VHS.Kurs4.store.artikel import Artikel


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

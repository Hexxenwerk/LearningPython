class Kuchen:
    mehl = 550

    def __init__(self, mehl: float, backpulver: float, zucker: float, backzeit: int, belag: list = None) -> None:
        self.mehl = Zutaten(name='mehl', menge=mehl)
        self.belag = belag
        self.zucker = Zutaten(name='zucker', menge=zucker)
        self.backzeit = backzeit
        self.backpulver = Zutaten(name='backpulver', menge=backpulver)

    def __str__(self) -> str:
        if self.belag is None:
            belag = ""
        else:
            belag = self.belag
        return f'Mehl: {self.mehl.menge} Backpulver: {self.backpulver.menge} ' \
               f'Zucker: {self.zucker.menge} Backzeit: {self.backzeit} ' \
               f'Belag: {", ".join([x for x in belag])}'

    def print_class_instance_attribute(self):
        print(f'Class Attribute für Mehl: {Kuchen.mehl}')
        print(f'Instance Attribute für Mehl: {self.mehl}')

    def print_belag(self) -> None:
        if self.belag is None:
            return None
        for nr, name in enumerate(self.belag):
            print(f'Belag Nr. {nr + 1}: {name}')

    def print_kalorien(self) -> None:
        print(f'Gesamte Kalorien des Kuchens: {self.kalorien_berechnen()}')

    def halbieren(self):
        self.backzeit = self.backzeit * 0.75
        self.mehl.menge = self.mehl.menge / 2
        self.zucker.menge = self.zucker.menge / 2
        self.backpulver.menge = self.backpulver.menge / 2
        return self

    def kalorien_berechnen(self) -> float:
        return self.mehl.kalorien * self.mehl.menge + \
               self.zucker.kalorien * self.zucker.menge + \
               self.backpulver.kalorien * self.backpulver.menge


class Zutaten:
    __kalorien = {
        'mehl': 4,
        'zucker': 4,
        'backpulver': 5.7,
    }

    def __init__(self, name: str, menge: float):
        self.name = name
        self.menge = menge
        self.kalorien = Zutaten.__kalorien[name]


def main():
    mein_kuchen1 = Kuchen(mehl=220, backpulver=0.50, zucker=70, backzeit=60)
    mein_kuchen2 = Kuchen(mehl=110, backpulver=0.25, zucker=35, backzeit=40, belag=['Pfirsich'])
    mein_kuchen3 = Kuchen(mehl=440, backpulver=1.00, zucker=90, backzeit=86, belag=['Kirschen', 'Birnen'])
    print(mein_kuchen1)
    print(mein_kuchen2)
    print(mein_kuchen3)
    mein_kuchen1.print_belag()
    mein_kuchen2.print_belag()
    mein_kuchen3.print_belag()
    mein_kuchen3.print_kalorien()
    mein_kuchen3.halbieren().print_kalorien()


if __name__ == '__main__':
    main()

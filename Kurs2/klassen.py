class Kuchen:
    butter = [220]

    def __init__(self, mehl: int, backpulver: float, zucker: int, backzeit: int) -> None:
        self.mehl = mehl
        self.backpulver = backpulver
        self.zucker = zucker
        self.backzeit = backzeit

    def zutaten(self):
        print(f'Mehl: {self.mehl} Backpulver: {self.backpulver} Zucker: {self.zucker} Backzeit: {self.backzeit}')

    def print_magic(self):
        print(self.butter)


def main():
    mein_kuchen1 = Kuchen(mehl=220, backpulver=0.50, zucker=70, backzeit=60)
    mein_kuchen2 = Kuchen(mehl=110, backpulver=0.25, zucker=35, backzeit=40)
    mein_kuchen3 = Kuchen(mehl=440, backpulver=1.00, zucker=90, backzeit=86)
    mein_kuchen1.zutaten()
    mein_kuchen2.zutaten()
    mein_kuchen3.zutaten()

    mein_kuchen1.butter[0] = 442
    print(mein_kuchen1.butter)
    print(mein_kuchen2.butter)
    print(Kuchen.butter)
    mein_kuchen2.print_magic()


if __name__ == '__main__':
    main()

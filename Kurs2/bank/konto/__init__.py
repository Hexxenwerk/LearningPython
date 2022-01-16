from random import randint

from Kurs2.bank.bank import Bank
from Kurs2.bank.person import Person


class Konto:
    def __init__(self, besitzer: Person, bank: Bank, kontostand=0, kontoart='giro'):
        self.kontoart = kontoart
        self.kontostand = kontostand
        self.kontonr = randint(10, 12)
        self.disporamen = 1000
        self.bank = bank
        self.besitzer = besitzer

    def __str__(self) -> str:
        return f'{self.besitzer.nachname} - Bank: {self.bank.name} - Kontostand: {self.kontostand}'

    def einzahlen(self, betrag: float = None):
        while betrag is None:
            try:
                betrag = float(input('Wie viel Geld möchten sie einzahlen? '))
            except ValueError:
                print('Der Betrag mss numerisch sein')
        self.kontostand += betrag

    def auszahlen(self, betrag: float = None):
        while betrag is None:
            try:
                betrag = float(input('Wie viel Geld möchten sie auszahlen? '))
            except ValueError:
                print('Der Betrag mss numerisch sein')
        self.kontostand -= betrag

    def auftrag(self, vorgang: str):
        if vorgang == 'transfer':
            zielkonto = input('Auf welches Konto soll überwiesen werden? ')
            try:
                betrag = float(input('Welcher Betrag soll überwiesen werden? '))
            except ValueError:
                print(f'Der Betrag muss numerisch sein')
            else:
                self.transfer(zielkonto=zielkonto, betrag=betrag)
        else:
            print(f'Vorgang "{vorgang}" nicht definiert')

    def transfer(self, zielkonto: str, betrag: float) -> None:
        if self.kontostand + self.disporamen < betrag:
            print('Der Kontostand und Disporamen ist nicht ausreichend')
            return None
        self.kontostand -= betrag
        print(f'{betrag} wurde and {zielkonto} überwiesen')

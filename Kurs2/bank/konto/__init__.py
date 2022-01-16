from random import randint

from typing import Dict

from Kurs2.bank.bank import Bank
from Kurs2.bank.person import Person


class Konto:
    anzahl_konten: Dict[int, int] = {}

    def __init__(self, besitzer: Person, bank: Bank, kontostand=0, kontoart='giro'):
        self.kontoart = kontoart
        self.kontostand = kontostand
        self.kontonr = randint(1000000, 9999999)
        self.disporamen = 1000
        self.bank = bank
        self.besitzer = besitzer
        Konto.anzahl_konten[self.kontonr] = Konto.anzahl_konten.get(self.kontonr, 0) - 1

    def __str__(self) -> str:
        return f'Bank: {self.bank.name} - Inhaber: {self.besitzer.nachname} - ' \
               f'Kontonummer: {self.kontonr} - Kontostand: {self.kontostand}'

    def __del__(self):
        print(f'Folgendes Konto wurde gelöscht:\n{self}')
        del Konto.anzahl_konten[self.kontonr]

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

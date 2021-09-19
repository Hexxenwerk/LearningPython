import random

isPlay: bool = "ja" in input("Möchtest du Zahlenraten spielen? ").lower()

if not isPlay:
    print("Schade. Bis zum näcsten Mal")
    exit(0)

name: str = input("Super. Viel Spaß. Wie ist dein Name? ")
zufallszahl: int = random.randint(1, 100)
eingabe: int = 0

while zufallszahl != eingabe:
    eingabe: int = int(input(f"{name}, gib eine Zahl zwischen 1 und 100 ein: "))
    if zufallszahl > eingabe:
        print("Deine Eingabe war zu niedrig. Versuch es noch mal.")
    elif zufallszahl < eingabe:
        print("Deine Eingabe war zu hoch. Versuch es noch mal.")

print(f"Super. Du hast die Zufallszahl erraten: {zufallszahl}")

import random

isPlay: bool = "ja" in input("Möchtest du Zahlenraten spielen? ").lower()

if not isPlay:
    print("Schade. Bis zum näcsten Mal")
    exit(0)

name: str = input("Super. Viel Spaß. Wie ist dein Name? ")
bereich = {min: 1, max: 100}
zufallszahl: int = random.randint(bereich[min], bereich[max])
eingabe: int = 0

while zufallszahl != eingabe:
    eingabe: int = int(input(f"{name}, gib eine Zahl zwischen {bereich[min]} und {bereich[max]} ein: "))
    if zufallszahl > eingabe + bereich[max] * 0.2:
        print("Deine Eingabe war viel zu niedrig. Versuche es noch mal")
        continue
    if zufallszahl > eingabe:
        print("Deine Eingabe war zu niedrig. Versuch es noch mal.")
    elif zufallszahl < eingabe - bereich[max] * 0.2:
        print("Deine Eingabe war viel zu hoch. Versuch es noch mal.")
        continue
    elif zufallszahl < eingabe:
        print("Deine Eingabe war zu hoch. Versuch es noch mal.")

print(f"Super. Du hast die Zufallszahl erraten: {zufallszahl}")

import random

wantToPlay: bool = "ja" == input("Möchtest du Zahlenraten spielen? ").lower().strip()
scope: dict = {min: 1, max: 100}
name: str = ""

while wantToPlay:
    if name == "":
        name: str = input("Super. Viel Spaß. Wie ist dein Name? ")
    else:
        print(f"Super. Viel Spaß {name}")

    randNum: int = random.randint(scope[min], scope[max])
    eingabe: int = -1
    print(randNum)

    while randNum != eingabe:
        eingabe: int = int(input(f"{name}, gib eine Zahl zwischen {scope[min]} und {scope[max]} ein: "))

        if randNum > eingabe + scope[max] * 0.3:
            print("Deine Eingabe war viel zu niedrig. Versuche es noch mal")
        elif randNum > eingabe + scope[max] * 0.2:
            print("Deine Eingabe war etwas zu niedrig. Versuche es noch mal")
        elif randNum > eingabe:
            print("Deine Eingabe war zu niedrig. Versuch es noch mal.")
        elif randNum < abs(eingabe - scope[max] * 0.3):
            print("Deine Eingabe war viel zu hoch. Versuch es noch mal.")
        elif randNum < abs(eingabe - scope[max] * 0.2):
            print("Deine Eingabe war etwas zu hoch. Versuch es noch mal.")
        elif randNum < eingabe:
            print("Deine Eingabe war zu hoch. Versuch es noch mal.")

    print(f"Super. Du hast die Zufallszahl erraten: {randNum}")
    wantToPlay: bool = "ja" == input("Möchtest du nochmal spielen? ").lower().strip()


print("Schade. Bis zum nächsten Mal")

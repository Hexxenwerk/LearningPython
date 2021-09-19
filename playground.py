zeit: str = input("Welche Tageszeit haben wir heute (Morgen/Mittag/Abend)? ").strip()
task: str = input("Welcher Beschäftigung gehst du nach (VHS-Kurs/frei/arbeiten)? ").strip()

isMorgen: bool = zeit.lower() == "morgen"
isMittag: bool = zeit.lower() == "mittag"
isAbend: bool = zeit.lower() == "abend"

if isMorgen:
    if task.lower().__contains__("vhs"):
        print("Ich programmiere")
    elif task.lower() == "frei":
        print("Ich frühstücke gemütlich")
    else:
        print(f"Die Beschäftigung {task.capitalize()} gibt es nicht am {zeit.capitalize()}")
elif isMittag:
    if task.lower() == "arbeiten":
        print("Ich muss am Computer arbeiten")
    elif task.lower() == "frei":
        print("Ich halte einen Mittagschlaf")
    else:
        print(f"Die Beschäftigung {task.capitalize()} gibt es nicht am {zeit.capitalize()}")
elif isAbend:
    if task.lower() == "arbeiten":
        print("Ich muss am Abend außer Haus arbeiten")
    elif task.lower() == "frei":
        print("Ich gehe schwimmen")
    else:
        print(f"Die Beschäftigung {task.capitalize()} gibt es nicht am {zeit.capitalize()}")
else:
    print(f"Die Tageszeit {zeit.capitalize()} steht nicht zur Verfügung")

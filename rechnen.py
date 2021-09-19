from math import ceil, floor


def div(a, b):
    if b == 0:
        print("Fehler: Teilen durch null (0) ist nicht zulässig")
        exit(1)
    return a / b


z1 = int(input("Gib eine Zahl ein: {:6}".format("")))
z2 = int(input("Gib noch eine Zahl ein: {:1}".format("")))

if z1 > z2:
    print(f"Zahl {z1} ist größer als {z2}")
elif z2 > z1:
    print(f"Zahl {z2} ist größer als {z1}")
else:
    print(f"Zahlen sind beide gleich groß: {z1}")

print("Die Potenz von {:-10} und {:-5} beträgt: {:>11}".format(z1, z2, z1 ** z2))
print("Die Division von {:-8} durch {:-3} beträgt: {:>11.8f}".format(z1, z2, div(z1, z2)))
print("Die Differenz von {:-7} und {:-5} beträgt: {:>11}".format(z1, z2, abs(z1 - z2)))
print("Das Produkt von {:-9} und {:-5} beträgt: {:>11}".format(z1, z2, z1 * z2))
print("Die größere Zahl von {:-4} und {:-5} lautet: {:>12}".format(z1, z2, max(z1, z2)))
print("Die kleinere Zahl von {:-3} und {:-5} lautet: {:>12}".format(z1, z2, min(z1, z2)))
print("Die untere Grenze von {:-3} und {:-5} lautet: {:>12}".format(z1, z2, floor(div(z1, z2))))
print("Die obere Grenze von {:-4} und {:-5} lautet: {:>12}".format(z1, z2, ceil(div(z1, z2))))

print("\nVerwendung von \"Backslash\" (\\): Tabulator:<Start>\t<Ende> und ein Signal: \b")

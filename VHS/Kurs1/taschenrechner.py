def div(a, b):
    if b == 0:
        print("Fehler: Teilen durch null (0) ist nicht zulässig")
        exit(1)
    return a / b


z1 = int(input("Gib die erste Zahl ein: {:2}".format("")))
z2 = int(input("Gib die zweite Zahl ein: {:1}".format("")))
op = input("Gib einen Operator ein: {:2}".format(""))

if op == "+":
    print(f"Die Summe von {z1} und {z2} beträgt: {z1 + z2}")
elif op == "-":
    print(f"Die Subtraktion von {z1} abzüglich {z2} beträgt: {z1 - z2}")
elif op == "*":
    print(f"Das Produkt von {z1} und {z2} beträgt: {z1 * z2}")
elif op == "/":
    print(f"Die Division von {z1} durch {z2} beträgt: {div(z1, z2)}")
elif op == "**":
    print(f"Die Potenz von {z1} hoch {z2} beträgt: {z1**z2}")
else:
    print(f"Fehler: '{op}' ist ein ungültiger Operator")

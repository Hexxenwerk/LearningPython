alle_zahlen = '- Alle Zahlen sind:'
alle_zahlen_positiv = '- Alle pos. Zahlen sind:'
alle_zahlen_negativ = '- Alle neg. Zahlen sind:'
alle_zahlen_summe = 0
anzahl_zahlen_positiv = 0

for durchlauf in range(-3, 8):
    eingabe = int(input('Gib eine Zahl ein: '))
    alle_zahlen += f' {eingabe}'
    alle_zahlen_summe += 1
    if eingabe > 0:
        alle_zahlen_positiv += f' {eingabe}'
        anzahl_zahlen_positiv += 1
    elif eingabe < 0:
        alle_zahlen_negativ += f' {eingabe}'

print(alle_zahlen)
print(alle_zahlen_positiv)
print(alle_zahlen_negativ)
print('- Summe aller Zahlen:', alle_zahlen_summe)
print('- Anzahl der pos. Zahlen:', anzahl_zahlen_positiv)

for x in range(10):
    if x == 5:
        break  # exits the loop
    else:
        print(x)
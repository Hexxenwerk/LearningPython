print('Willkommen bei EIDEICAR online-Shop')

knd_name = input('Wie ist ihr Name? ').lower()
knd_plz = input('Wie ist ihre PLZ? ')
warenkorb = []
eingabe = ""

print(f'Hallo {knd_name}. Geben sie ihre Einkaufswünsche ein und "exit", um zur Kasse zur gelangen:')

while eingabe != 'exit':
    eingabe = input('Artikel oder "exit": ').lower()
    if eingabe != 'exit':
        warenkorb.append(eingabe)
    else:
        print('Sie werden jetzt zur Kasse weitergeleitet.')

with open('rechnung.txt', mode='w') as ausgabe_datei:
    ausgabe_datei.write(f'Rechnung für {knd_name.title()}:\n')
    print(f'Rechnung für {knd_name.title()}:')
    for artikel_position in range(len(warenkorb)):
        ausgabe_zeile = f'{artikel_position + 1}. {warenkorb[artikel_position].capitalize()}'
        ausgabe_datei.write(ausgabe_zeile + '\n')
        print(ausgabe_zeile)

print(f'Vielen Dank für ihren Besuch')

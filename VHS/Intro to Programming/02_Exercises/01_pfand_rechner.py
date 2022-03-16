""" Pfandrechner """
####################

# 0. Configuration / Setting Phase - Constants
PFAND_GLAS = 0.08
PFAND_PLASTIK = 0.25

# 1. Welcome Message
print('Willkommen in ihrem Supermarkt')

# 2. Eingabe
anzahl_glas = int(input('Wie viele Glasflaschen? '))
anzahl_plastik = int(input('Wie viele Plastikflaschen? '))

# 3. Verarbeitung
summe = str(round(PFAND_GLAS * anzahl_glas + PFAND_PLASTIK * anzahl_plastik, 2)).replace('.', ',')

# 4. Ausgabe
print(f'Ihr Guthaben beträgt: € {summe}')

# age >= 18
# payment_method = True
# items = 5

age = 18
paymnet_method = True
items = 2
nicht_erfuellt = ""

if not age >= 18:
    nicht_erfuellt += '- Du bist zu jung\n'

if not paymnet_method:
    nicht_erfuellt += '- Bezahlmethode nicht vorhanden\n'

if not items > 0:
    nicht_erfuellt += '- Du musst Produkte auswählen\n'

if not len(nicht_erfuellt):
    print('Bitte zur Kasse')
else:
    print('Folgende Anforderungen wurden nicht erfüllt:\n' + nicht_erfuellt)

# age >= 18
# payment_method = True
# items = 5

age = 35
paymnet_method = True
items = 5
nicht_erfuellt = []

if not age >= 18:
    nicht_erfuellt.append('Du bist zu jung')

if not paymnet_method:
    nicht_erfuellt.append('Bezahlmethode nicht vorhanden')

if items > 0:
    nicht_erfuellt.append('Du musst Produkte abholen')

print('Folgende Anforderungen wurden nicht erfüllt:', nicht_erfuellt)

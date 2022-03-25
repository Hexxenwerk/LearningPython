from typing import List

menu = {
    1: {
        'type': 'food',
        'name': 'Margherita',
        'price': 5.0,
        'category': 'Pizza',
    },
    2: {
        'type': 'food',
        'name': 'Thunfisch',
        'price': 6.0,
        'category': 'Pizza',
    },
    3: {
        'type': 'food',
        'name': 'Salami',
        'price': 7.0,
        'category': 'Pizza',
    },
    10: {
        'type': 'food',
        'name': 'Nudeln',
        'price': 5.0,
        'category': 'Auflauf',
    },
    11: {
        'type': 'food',
        'name': 'Kartoffeln',
        'price': 6.0,
        'category': 'Auflauf',
    },
    20: {
        'type': 'food',
        'name': 'Normal',
        'price': 3.0,
        'category': 'Salat',
    },
    21: {
        'type': 'food',
        'name': 'Cesar',
        'price': 4.0,
        'category': 'Salat',
    },
    100: {
        'type': 'drink',
        'name': 'Cola',
        'price': 3.0,
        'category': None,
    },
    101: {
        'type': 'drink',
        'name': 'Fanta',
        'price': 2.0,
        'category': None,
    },
    102: {
        'type': 'drink',
        'name': 'Wasser',
        'price': 1.0,
        'category': None,
    },
}
cart: List[int] = []  # storing customer orders
total: float = 0.0  # sum of all ordered goods

print('\nWillkommen bei Acasa\n')
print('Geben sie eine Nummer ein oder "0" um zu den Getränken zu gelangen:\n')

for num, rr in sorted(menu.items()):
    if rr.get('type') == 'food':
        print(f'{num:-4}. {rr["category"]:10} {rr["name"]:25} Preis in € {rr["price"]:>5.2f}')

while True:
    selection = int(input('Selektion: '))
    if not selection:
        print('Sie werden jetzt zur Getränkeauswahl weitergeleitet.')
        break
    if selection not in menu or menu[selection].get('type') != 'food':
        print(f'Eingabe "{selection}" steht in unseren Speisen nicht zur Auswahl.')
        continue
    cart.append(selection)

for num, rr in sorted(menu.items()):
    if rr.get('type') == 'drink':
        print(f'{num:-4}. {" ":10} {rr["name"]:25} Preis in € {rr["price"]:>5.2f}')

while True:
    selection = int(input('Selektion: '))
    if not selection:
        print('Sie werden jetzt zum Warenkorb weitergeleitet.')
        break
    if selection not in menu or menu[selection].get('type') != 'drink':
        print(f'Eingabe "{selection}" steht in unseren Getränken nicht zur Auswahl.')
        continue
    cart.append(selection)

print(f'\nIhre Bestellung an Speisen und Getränken:')

# Output of ordered meals first
for num in cart:
    if menu[num].get('type') == 'food':
        print(f'{num:-4}. {menu[num]["category"]:10} {menu[num]["name"]:25} Preis in € {menu[num]["price"]:>5.2f}')

# Output of ordered drinks
for num in cart:
    if menu[num].get('type') == 'drink':
        print(f'{num:-4}. {" ":10} {menu[num]["name"]:25} Preis in € {menu[num]["price"]:>5.2f}')

print(f'Summe aller Speisen und Getränke: {" ":8} Preis in € {sum([menu[n]["price"] for n in cart]):>5.2f}')

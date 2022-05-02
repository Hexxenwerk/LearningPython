abc = 'abcdefghijklmnopqrstuvwxyz'
cipher = ""
shift = ""

while not shift.isdecimal() or not 0 <= int(shift) <= 25:
    print('You need to enter a number between 0 and 25!')
    shift = input('Please enter the number of places to shift: ')

shift = int(shift)
text = input('Please enter a sentence: ')

for c in text:
    c = c.lower()
    if c in abc:
        idx = abc.find(c) + shift
        if idx >= len(abc):
            idx %= len(abc)
        c = abc[idx]
    cipher += c

print(f'The encrypted sentence is: {cipher}')

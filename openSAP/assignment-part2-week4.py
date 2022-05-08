with open('secret.txt', 'r') as file:
    secret = [field.strip() for field in file]

with open('key.txt', 'r') as file:
    columns, rows = [int(field.strip()) for field in file]

with open('public.txt', 'w') as file:
    for row in range(rows):
        print(''.join(secret[columns * row:columns * (row + 1)]), file=file)

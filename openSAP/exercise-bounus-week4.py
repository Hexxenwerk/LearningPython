with open('player1.txt', 'r') as file:
    player1 = [line.strip() for line in file]

with open('player2.txt', 'r') as file:
    player2 = [line.strip() for line in file]

result = {'player1': 0, 'player2': 0, 'draw': 0}

for p1, p2 in zip(player1, player2):
    if p1 == p2:
        result["draw"] += 1
    elif p1 == 'R' and p2 == 'S':
        result["player1"] += 1
    elif p1 == 'S' and p2 == 'P':
        result["player1"] += 1
    elif p1 == 'P' and p2 == 'R':
        result["player1"] += 1
    else:
        result["player2"] += 1

with open('result.txt', 'w') as file:
    print(f'Player1 wins: {result["player1"]}', file=file)
    print(f'Player2 wins: {result["player2"]}', file=file)
    print(f'Draws: {result["draw"]}', file=file)

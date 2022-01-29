def addieren_1(x: int, y: int):
    result: int = x + y
    print("Ergebnis:", result)


def addieren_2(x: int, y: int) -> int:
    return x + y


def addieren_3(x: int, y: int):
    return "Das Ergebnis beträgt:", x + y


addieren_1(5, 8)
total: int = addieren_2(50, 60)
print("Total:", total)

msg, total = addieren_3(500, 600)
print(msg, total)

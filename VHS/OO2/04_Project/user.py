def get_line_count() -> int:
    try:
        return int(input("Gib die Anzahl der zu übersetzenden Zeilen ein: "))
    except ValueError:
        print("Du musst eine numerische Eingabe vornhemen.")
        return get_line_count()


def cli_input() -> tuple:
    path = input("Gib den Pfad ein, der nach Dateien durchsucht werden soll ['.']: ")
    selector = input("Gib einen Selektor an oder Enter für [*.txt]: ")
    line_count = get_line_count()
    return path, selector, line_count

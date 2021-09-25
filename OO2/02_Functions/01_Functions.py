def greeting(name: str, years: int = 0):
    print(f'Hello {name}')
    print(f'Du hast {years} Hintergrund in Softwareentwicklung.')
    print('Warum besuchst du Python Kurs 2?')


def get_background_years():
    try:
        years: int = int(input("Wie viele Jahre programmierst du schon? "))
        return years
    except ValueError:
        print("Die Eingabe muss numerisch sein.")
        return get_background_years()


def main():
    name: str = input("Wie ist dein Name? ")
    years = get_background_years()
    greeting(name, years)


exit(main())

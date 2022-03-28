def greeting(**kwargs):
    print(kwargs)


def main():
    greeting(first_name="Thomas", kids=3, age=36, anwesend=True)
    greeting(car="VW", apfel="Banane")


if __name__ == '__main__':
    main()

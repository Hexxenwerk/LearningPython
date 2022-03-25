def greeting_4(first_name: str, last_name: str, plz: str = "00000"):
    print(f'Hallo {first_name} {last_name} living at {plz}')


def main():
    greeting_4('Sabine', 'Meier', '12345')


if __name__ == '__main__':
    main()

# without parameters
def greeting_1():
    print('Hallo Dude')


# with single parameter
def greeting_2(name: str):
    print(f'Hallo {name}')


# with multiple parameters
def greeting_3(first_name, last_name):
    print(f'Hallo {first_name} {last_name}')


# with default value for plz
def greeting_4(first_name, last_name, plz="00000"):
    print(f'Hallo {first_name} {last_name} living at {plz}')


def main():
    greeting_1()
    greeting_2('Thomas')
    greeting_2('Ingo')
    greeting_2('Sven')
    greeting_3('Sara', 'Meier')
    greeting_3('Lena', 'Meier')
    greeting_3('Julia', 'Meier')
    greeting_3('Meier', 'Steffi')  # "Hallo Meier Steffi"
    greeting_3(last_name='Meier', first_name='Steffi')  # "Hallo Steffi Meier"
    greeting_4('Sabine', 'Meier')  # "Hallo Sabine Meier living at 00000"
    greeting_4('Sabine', 'Meier', '12345')  # "Hallo Sabine Meier living at 12345"


if __name__ == '__main__':
    main()

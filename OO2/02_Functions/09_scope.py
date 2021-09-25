location: str = 'Hamburg'


def greeting_1(user_name: str):
    print(f"Hello {user_name} von {location}")


def greeting_2(user_name: str):
    location: str = "Berlin"
    print(f"Hello {user_name} von {location}")


def greeting_3(user_name: str):
    global location
    location = "Aachen"
    print(f"Hello {user_name} von {location}")


greeting_1("Ingo")
greeting_2("Sara")
greeting_3("Lena")
print(location)
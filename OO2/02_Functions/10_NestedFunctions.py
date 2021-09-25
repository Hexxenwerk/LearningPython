y: int = 20


def greeting(user_name: str):
    print(f"Hello {user_name}")

    x: int = 10

    def function2():
        print("Hello inner function")

        user_name: str = "Sarah"
        print(f"Hello {user_name}")
        print(x)
        print(y)

    function2()
    print(f"Willkommen {user_name}")


greeting("Sara")


# Closure:
def global_function(name: str):
    def local_function():
        print(f"Hello {name}")

    return local_function


ref_function = global_function("Lena")
print(ref_function)


def power_generator(num):
    def power_n(power):
        return num ** power

    return power_n


power_two = power_generator(2)
print(power_two(8))

power_three = power_generator(3)
print(power_two(3))
print(power_two(5))

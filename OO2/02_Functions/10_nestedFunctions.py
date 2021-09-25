y: int = 20


def my_outer_function(user_name: str):
    print(f"Hello {user_name}")

    x: int = 10

    def my_inner_function():
        print("Hello innter function")

        user_name: str = "Sarah"
        print(f"Hello {user_name}")
        print(x)
        print(y)

    my_inner_function()
    print(f"Willkommen {user_name}")


my_outer_function("Sara")


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
x: int = 5
y: int = 100


def outer():
    x: int = 10

    def inner():
        nonlocal x
        global y
        x = 20
        y = 200
        print(f"inner x: {x}")

    inner()
    print(f"outer x: {x}")


print(f"global x: {x}")
outer()
print(f"global x: {x}")
print(f"y: {y}")

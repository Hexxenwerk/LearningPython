def greeting(**container):
    print(container, type(container))
    for key, val in container.items():
        print(key, val)

    print()


greeting(first_name="Ingo", last_name="Meier")
greeting(first_name="Lena", last_name="Meier", car="Audi")
greeting(kz="B-MK-123", color="Red", temperature=32.7)

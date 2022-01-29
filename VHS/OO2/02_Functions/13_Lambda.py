def multiplier(n):
    return n * 2


print(multiplier(5))

doubler = lambda n: n * 2
print(doubler(5))

addieren = lambda x, y: x + y
print(addieren(1, 3))


#############

def myfunc(n):
    return lambda a: a ** n


my_doubler = myfunc(2)
print(my_doubler(5))

my_tripler = myfunc(3)
print(my_doubler(5))

items = [
    ("Product 1", 15),
    ("Product 2", 4),
    ("Product 3", 50),
    ("Product 4", 2),
]

items.sort(key=lambda item: item[1])
print(items)

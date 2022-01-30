class Teilnehmner:
    discount = 10
    num_of_instance = 0

    def __init__(self, first_name: str, last_name: str, city: str, car=""):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.car = car
        self.paymnent_method = ""

        Teilnehmner.num_of_instance += 1

    def set_paymnet_method(self, payment_method: str):
        self.paymnent_method = payment_method

    def show_information(self):
        print(f"First Name: {self.first_name}, Last Name: {self.last_name}, Payment method: {self.paymnent_method} ")


t1 = Teilnehmner("Ingo", "Maier", "Hamburg", "Audi")
t2 = Teilnehmner("Sara", "Maier", "Hamburg", "Tesla")

t1.set_paymnet_method("Paypal")
t2.set_paymnet_method("Master Card")

t1.show_information()
t2.show_information()

print(t1.paymnent_method)
print(t2.paymnent_method)

print(t1.__dict__)
print(t2.__dict__)

print(t1.discount)
print(t2.discount)
print()

t1.discount = 20

print(t1.discount)
print(t2.discount)
print()

Teilnehmner.discount = 50

print(t1.discount)
print(t2.discount)
print()

print(Teilnehmner.num_of_instance)
t3 = Teilnehmner("Liane", "Maier", "Hamburg", "VW")
print(Teilnehmner.num_of_instance)

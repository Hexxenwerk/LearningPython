class Teilnehmner:
    def __init__(self, first_name: str, last_name: str, city: str, car=""):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.car = car
        self.paymnent_method = ""


t1 = Teilnehmner("Ingo", "Maier", "Hamburg", "Audi")
t2 = Teilnehmner("Sara", "Maier", "Hamburg", "Tesla")
t3 = Teilnehmner("Liane", "Maier", "Hamburg")

liste_teilnehmende = []
liste_teilnehmende.append(t1)
liste_teilnehmende.append(t2)
liste_teilnehmende.append(t3)

counter = 1

for tn in liste_teilnehmende:
    print(f"{counter}: . {tn.first_name} {tn.car}")
    counter += 1

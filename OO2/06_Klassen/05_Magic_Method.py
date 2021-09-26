class Teilnehmer:
    def __init__(self, first_name: str, last_name: str, salary: int, temperature: float):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.temperature = temperature

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.salary}"

    def __eq__(self, other):
        return self.salary == other.salery

    def __gt__(self, other):
        return self.temperature == other.temperature


t1 = Teilnehmer("Ingo", "Maier", 70000, 39)
t2 = Teilnehmer("Sara", "Maier", 71000, 37.6)

print(t1)
print(t2)

if t2 > t1:
    print(f"{t2.first_name} verdient mehr als {t2.first_name}")

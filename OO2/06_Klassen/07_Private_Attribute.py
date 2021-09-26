class Teilnehmer:
    __company = "VHS"

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.__bonus = 500


t1 = Teilnehmer("Ingo", "Maier")

# Show instance-based private attribute:
print(t1.first_name, t1.last_name, t1._Teilnehmer__bonus)
print(t1.__dict__)
t1._Teilnehmer__bonus = 700
print(t1.__dict__)

# Show the class-based private attribute
print(t1._Teilnehmer__company)

# Change the class-based private attribute
t1._Teilnehmer__company = "Lufthansa"

# Show the class-based private attribute
print(t1._Teilnehmer__company)

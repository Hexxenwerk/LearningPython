class Teilnehmner:
    def __init__(self, first_name: str):
        self.teilnehmner_name = first_name

    def show_name(self):
        print(f"Hello {self.teilnehmner_name}")

    def paymnent(self):
        print(f"Payment for: {self.teilnehmner_name}")


t1 = Teilnehmner("Ingo")
t2 = Teilnehmner("Sara")

t1.show_name()
t2.show_name()

t1.teilnehmner_name = "Idiot"

t1.paymnent()
t2.paymnent()
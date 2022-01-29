class Car:
    def __init__(self, kz: str, color: str, model: str) -> None:
        self.kz = kz
        self.color = color
        self.model = model

    def parking(self):
        print(f"I am parking my {self.model}")

    def cleaning(self):
        print(f"I am cleaning my {self.model}")


class Audi(Car):
    def __init__(self, kz: str, color: str, model: str, gps: bool) -> None:
        super().__init__(kz, color, model)
        self.gps = gps

    def gps_navigate(self):
        print("I am navigating")


class VW(Car):
    def __init__(self, kz: str, color: str, model: str, schiebedach: bool) -> None:
        super().__init__(kz, color, model)
        self.schiebedach = schiebedach

    def schiebedach_open(self):
        print("Opening Panorama Window")


class Tesla(Car):
    def __init__(self, kz: str, color: str, model: str, battery: bool) -> None:
        super().__init__(kz, color, model)
        self.battery = battery

    def charge_battery(self):
        print("I am recharging")


vw_passat = VW("F-TR-123", "red", "Passat", True)
audi_1 = Audi("K-ZA-987", "green", "A4", True)

print("Ende")

vw_passat.cleaning()
audi_1.cleaning()

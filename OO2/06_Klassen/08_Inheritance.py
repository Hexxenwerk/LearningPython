class Car:
    def __init__(self, kz: str, color: str, model: str) -> None:
        self.kz = kz
        self.color = color
        self.model = model

    @staticmethod
    def parking():
        print("I am parking")

    @staticmethod
    def cleaning():
        print("I am cleaning")


class Audi(Car):
    def __init__(self, kz: str, color: str, model: str, gps: bool) -> None:
        super().__init__(kz, color, model)
        self.gps = gps

    @staticmethod
    def gps_navigate():
        print("I am navigating")


class VW(Car):
    def __init__(self, kz: str, color: str, model: str, schiebedach: bool) -> None:
        super().__init__(kz, color, model)
        self.schiebedach = schiebedach

    @staticmethod
    def schiebedach_open():
        print("Opening Panorama Window")


class Tesla(Car):
    def __init__(self, kz: str, color: str, model: str, battery: bool) -> None:
        super().__init__(kz, color, model)
        self.battery = battery

    @staticmethod
    def charge_battery():
        print("I am recharging")


vw_passat = VW("F-TR-123", "red", "Passat", True)
audi_1 = Audi("K-ZA-987", "green", "A4", True)

print("Ende")

vw_passat.cleaning()
audi_1.cleaning()

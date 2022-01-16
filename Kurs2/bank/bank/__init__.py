class Bank:
    def __init__(self, name: str, firmensitz: str, land: str, blz: int, bic: str):
        self.blz = blz
        self.bic = bic
        self.land = land
        self.firmensitz = firmensitz
        self.name = name

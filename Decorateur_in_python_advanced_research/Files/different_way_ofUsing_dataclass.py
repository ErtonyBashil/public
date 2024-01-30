class Tatavoiture:
    def __init__(self, town: str, distance: float, pricekm: float):
        self.town = town
        self.distance = distance
        self.pricekm = pricekm


v1 = Tatavoiture("Dakar", 12.5, 900)
print(v1 == Tatavoiture("Dakar", 12.5, 900))


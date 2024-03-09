class Tatavoiture:
    def __init__(self, town: str, distance: float, pricekm: float):
        self.town = town
        self.distance = distance
        self.pricekm = pricekm

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.town, self.distance, self.pricekm) == (other.town, other.distance, other.pricekm)


v1 = Tatavoiture("Dakar", 12.5, 900)
print(v1.pricekm)
# we try to print
print(v1)
# We initialize the object
print(v1 == Tatavoiture("Dakar", 12.5, 900))
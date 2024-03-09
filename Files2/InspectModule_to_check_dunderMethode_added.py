class Tatavoiture:
    def __init__(self, town: str, distance: float, pricekm: float):
        self.town = town
        self.distance = distance
        self.pricekm = pricekm


v1 = Tatavoiture("Dakar", 12.5, 900)
print(v1.pricekm)
# we try to print 
print(v1)
# We initialize the object
print(v1 == Tatavoiture("Dakar", 12.5, 900))

# The representation of the objects is not very descriptive using the standar classes
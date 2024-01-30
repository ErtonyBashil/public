from collections import namedtuple

NamedTupleTata = namedtuple("NamedTupleTata", ["town", "distance", "pricekm"])
Tatavoiture = NamedTupleTata("Dakar", 12.5, 900)
print(Tatavoiture.town)
print(Tatavoiture)
print(Tatavoiture == NamedTupleTata("Dakar", 12.5, 900))

## DATACLASS ALTERNATIVE NamedTuple


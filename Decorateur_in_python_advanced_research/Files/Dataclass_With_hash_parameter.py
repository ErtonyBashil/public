from dataclasses import dataclass

@dataclass(frozen=True)
class Tatavoiture:
    town: str
    distance: bool
    pricekm: float

v1 = Tatavoiture("Dakar", 12.5, 900)
v1.distance = 22.5
print(v1)

# As we set our Frozen parameter True, we can not modify our object is throw an error
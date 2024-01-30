from dataclasses import dataclass

@dataclass(kw_only=True)
class Tatavoiture:
    town: str
    distance: float
    pricekm: float


v1 = Tatavoiture(town = "Dakar", distance = 12.5, pricekm = 900)
print(v1.town)

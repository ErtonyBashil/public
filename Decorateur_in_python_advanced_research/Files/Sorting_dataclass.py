import dataclasses as dataclass


@dataclass(order=True)
class Tatavoiture:
    sort_index: int = field(init=False, repr=False)
    town: str
    distance: float
    pricekm: float

    def __post_init__(self):
        self.sort_index = self.pricekm


v1 = Tatavoiture("Kigali", 1700, 1050.0)
v2 = Tatavoiture("Nairobi", 2500, 1000.5)
print(v1 > v2)

##  The distance is False, as we all know that the distance 2500 is greater than 1700.
## We use __ post-init__ to make an brieve comparaison of the second argument
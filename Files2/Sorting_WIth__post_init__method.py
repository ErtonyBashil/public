import dataclasses as dataclass

@dataclass(order= True, unsafe_hash=True)
class Tatavoiture:
    sort_index: int = field(init=False, repr=False)
    town: str
    distance: float
    pricekm: float

    def __post_init__(self):
        self.sort_index = self.pricekm


v1 = Tatavoiture("Kigali", 1700, 1050.0)
v2 = Tatavoiture("Kigali", 1700, 1050.0)
v3 = Tatavoiture("Nairobi", 2500, 1000.5)
print(hash(v1))
print(hash(3))
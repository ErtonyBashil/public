```python
from dataclasses import dataclass

@dataclass(order=True)
class Tatavoiture:
    town: str
    distance: float
    pricekm: float


v1 = Tatavoiture("Kigali", 1700, 1050.0)
v1 = Tatavoiture("Nairobi", 2500, 1000.5)
print(v1>v2)

# SORTING, ORDERING
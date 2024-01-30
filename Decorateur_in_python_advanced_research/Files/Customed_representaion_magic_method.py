from dataclasses import dataclass

@dataclass
class Tatavoiture:
    town:str = 'Dakar'
    distance: float = 2000.5
    pricekm: float = 12.5

print(Tatavoiture())
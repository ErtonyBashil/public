from dataclasses import dataclass

@dataclass
class Tatavoiture:
    town: str
    distance: float
    pricekm: float
    year: int


@dataclass
class Driver(Tatavoiture):
    name: str
    num: int
    salary: float

## we can create an object of the driver class using all the attributes of theTatavoiture class

print(Driver("Libreville", 450.5, 1500, "Mr Patrick", 20345094, 2000000.0))
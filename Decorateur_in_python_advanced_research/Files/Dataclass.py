from dataclasses import dataclass

@dataclass
class Tatavoiture:
    town: str
    distance: bool
    pricekm: float

    # def prixcourse(self):
    #     return self.distance * self.pricekm


v1 = Tatavoiture("Dakar", 12.5, 900)
print(v1.town)

==================================================
from dataclasses import dataclass
@dataclass
class Tatavoiture:
    town:str = 'Dakar'
    distance: float = 2000.5
    pricekm: float = 12.5


print(Tatavoiture())
======================================================
class Tatavoiture:
    def __init__(self, town: str, distance: float, pricekm: float):
        self.town = town
        self.distance = distance
        self.pricekm = pricekm

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(Town ={self.town!r}, distance= {self.distance!r}, Prix = {self.pricekm!r})')


voiture1 = Tatavoiture('Goma', 6002.7, 200000)
====================================================================

from dataclasses import dataclass


@dataclass
class Tatavoiture:
    town: str
    distance: float
    pricekm: float
    dimension: Tuple
    year: int


print(Tatavoiture('Kinshasa', 1.27, 2000.0, (3.235, -1.999)))

print("===============================================================")

from dataclasses import dataclass

@dataclass
class Tatavoiture:
    town: str
    distance: bool
    pricekm: float

    # def prixcourse(self):
    #     return self.distance * self.pricekm


v1 = Tatavoiture("Dakar", 12.5, 900)
print(v1 == Tatavoiture("Dakar", 12.5, 900))

print("===============================================================")

from dataclasses import dataclass

@dataclass
class Tatavoiture:
    town: str
    distance: bool
    pricekm: float

v1 = Tatavoiture("Dakar", 12.5, 900)
v1.distance = 22.5
print(v1)
print("===============================================================")

from dataclasses import dataclass

@dataclass(frozen = True)
class Tatavoiture:
    town: str
    distance: bool
    pricekm: float

class Driver:
    name: str
    num: int
    salary :float
v1 = Tatavoiture("Dakar", 12.5, 900)
v1.distance = 22.5
print(v1)
print("===============================================================")

from dataclasses import dataclass

@dataclass
class Tatavoiture:
    town: str
    distance: float
    pricekm: float

@dataclass
class Driver(Tatavoiture):
    name: str
    num: int
    salary: float


print(Driver("Libreville", 450.5, 1500, "Mr Patrick", 20345094, 2000000.0))
print("===============================================================")

from dataclasses import dataclass, KW_ONLY

@dataclass
class Tatavoiture:
    town: str
    _: KW_ONLY
    distance: float
    pricekm: float


v1 = Tatavoiture("Dakar", 12.5, 900.6)
print(v1)
======================================================

@dataclass(order=True, unsafe_hash=True)
class Tatavoiture:
    sort_index: int = field(init=False, rep=False)
    town: str
    distance: float
    pricekm: float

    def __post_init__(self):
        slef.sort_index = self.pricekm


v1 = Tatavoiture("Kigali", 1700, 1050.0)
v1 = Tatavoiture("Nairobi", 2500, 1000.5)
print(hash(v1))
print(hash(v3))

print('========================================================')

from dataclasses import dataclass, field

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
print(hash(v2))

print('========================================================')

Tatavoiture_tuple = ("Dakar", 12.5, 900)
Tatavoiture_dict = {"town": "Dakar", "distance": 12.5, "pricekm": 900}

print(Tatavoiture_tuple[0])
print(Tatavoiture_dict['distance'])
==============================================================

from collections import namedtuple

NamedTupleTata = namedtuple("NamedTupleTata", ["town", "distance", "pricekm"])
Tatavoiture = NamedTupleTata("Dakar", 12.5, 900)
print(Tatavoiture.town)
print(Tatavoiture)
print(Tatavoiture == NamedTupleTata("Dakar", 12.5, 900))
print("========================================================================")

from collections import namedtuple

NamedTupleTata = namedtuple("NamedTupleTata", ["town", "distance", "pricekm"])

v1= namedtuple("v1", ["model", "size", "kilometrage"])
v2 = NamedTupleTata("Dakar", 12.5, 900)
print(v2 ==v1("Dakar", 12.5, 900))

v2.town = "Kinshansa"
print("========================================================================")




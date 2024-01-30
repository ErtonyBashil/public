from collections import namedtuple


NamedTupleTata = namedtuple("NamedTupleTata", ["town", "distance", "pricekm"])

v1= namedtuple("v1", ["model", "size", "kilometrage"])
v2 = NamedTupleTata("Dakar", 12.5, 900)
print(v2 ==v1("Dakar", 12.5, 900))
v2.town = "Kinshasa"


#### The error is thrown because we can not set a default value.
## No modification because of the restriction

import attr
# we have to import the library

@attr.s
class Tatavoiture:
    town = attr.ib()
    distance = attr.ib()
    pricekm = attr.ib()

v1 = Tatavoiture("Dakar", 12.5, 8000.5)
print(v1.town)
print(v1)
print(v1==Tatavoiture("Dakar", 12.5, 8000.5))

## Attr is another challenging and promising alternative of dataclass
## However, is not part of the standard library
from dataclasses import dataclass, KW_ONLY
# we have to import the KW_ONLY


@dataclass(kw_only=True)
class Tatavoiture:
    town: str
    distance: float
    pricekm: float


v1 = Tatavoiture("Dakar", 12.5, 900)
print(v1.town)


## The error eccurs because the KW_ONLY constrains us to specify the arguments


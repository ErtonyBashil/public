class Tatavoiture:
    def __init__(self, town:str, distance:float, pricekm:float):
        self.town = town
        self.distance = distance
        self.pricekm = pricekm

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(Town ={self.town!r}, distance= {self.distance!r}, {self.pricekm!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.town, self.distance, self.pricekm) == (other.town, other.distance, other.pricekm)

    def prixcourse(self):
        return self.distance * self.pricekm


v1 = Tatavoiture("Dakar", 12.5, 900)

#v2 = Tatavoiture("Dakar", 3, 2000)

print(v1.pricekm)
print(v1)
print(v1 == Tatavoiture("Dakar", 12.5, 900))




    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)
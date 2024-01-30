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
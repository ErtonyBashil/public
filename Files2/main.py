import os

def make_commit(days: int):
    if days < 1:
        # Push command
        return os.system('git push')
    else:
        dates = f'{days} days ago'

        with open('data.txt', 'a') as file:
            file.write(f'{dates} <-This was the commit for the day\n')

            #staging
            os.system('git add data.txt')

            # commit
            os.system('git commit --date="'+dates+'" -m "Daily commit"')

            return days * make_commit(days-1)

make_commit(150)

print(================================================================)
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
print(hash(v3))
print(=======================================================================)
from Organism import Organism

import random

class Plant(Organism):

    def __init__(self, x,y,age,power,init,photo,type):
        super().__init__(x,y,age,power,init,photo,type)

    def action(self, world):

        dir = random.randint(0,99)

        if dir < 3:
            world.multiplication(self)




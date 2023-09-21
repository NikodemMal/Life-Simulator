from Organism import Organism

class Ground(Organism):
    def __init__(self,x=0,y=0,age=0,power=0,init=0,photo="ground.png",type='g'):
        super().__init__(x,y,age,power,init,photo,type)

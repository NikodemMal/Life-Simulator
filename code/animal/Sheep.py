from animal.Animal import Animal

class Sheep(Animal):
    def __init__(self,x,y,age=0,power=4,init=4,photo="sheep.png",type='s'):
        super().__init__(x,y,age,power,init,photo,type)

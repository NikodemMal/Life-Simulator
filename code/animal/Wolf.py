from animal.Animal import Animal

class Wolf(Animal):
    def __init__(self,x,y,age=0,power=9,init=5,photo="wolf.png",type='w'):
        super().__init__(x,y,age,power,init,photo,type)

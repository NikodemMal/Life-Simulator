from plants.Plant import Plant

class Grass(Plant):
    def __init__(self,x,y,age=0,power=0,init=0,photo="grass.png",type='$'):
        super().__init__(x,y,age,power,init,photo,type)
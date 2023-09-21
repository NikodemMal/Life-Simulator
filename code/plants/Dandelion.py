from plants.Plant import Plant

class Dandelion(Plant):
    def __init__(self,x,y,age=0,power=0,init=0,photo="dandelion.png",type='d'):
        super().__init__(x,y,age,power,init,photo,type)

    def action(self, world):
        super().action(world)
        super().action(world)
        super().action(world)


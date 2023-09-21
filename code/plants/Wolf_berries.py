from plants.Plant import Plant

class Wolf_berries(Plant):
    def __init__(self,x,y,age=0,power=99,init=0,photo="wolf_berries.png",type='&'):
        super().__init__(x,y,age,power,init,photo,type)

    def collision(self,attacked,world,number):
            if number == 1:
                #attacked atakowany
                attacked.collision(self,world,0)
            else:
                #attacked - atakujacy
                if self.get_power() <= attacked.get_power():
                    world.remove(attacked, self, False)
                    world.remove(self,attacked,False)
                else:
                    world.remove(attacked,self,False)
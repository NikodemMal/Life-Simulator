from plants.Plant import Plant

class Guarane(Plant):
    def __init__(self,x,y,age=0,power=0,init=0,photo="guarane.png",type='%'):
        super().__init__(x,y,age,power,init,photo,type)

    def collision(self,attacked,world,number):
            if number == 1:
                #attacked atakowany
                attacked.collision(self,world,0)
            else:
                #attacked - atakujacy
                if self.get_power() <= attacked.get_power():
                    attacked.set_power(attacked.get_power()+3)
                    world.remove(self,attacked,True)
                else:
                    world.remove(attacked,self,False)
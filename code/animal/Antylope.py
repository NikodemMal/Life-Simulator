from animal.Animal import Animal
import random

class Antylope(Animal):
    def __init__(self,x,y,age=0,power=4,init=4,photo="antylope.png",type='a'):
        super().__init__(x,y,age,power,init,photo,type)

    def action(self, world):
        super().action(world)
        list = world.get_list()
        if self in list:
            super().action(world)

    def collision(self,attacked,world,number):
        roll = random.randint(0, 99)
        if number == 1:
            # attacked atakowany
            if roll < 50:
                attacked.collision(self, world, 0)
            else:
                print("antylopa uciekla")
        else:
            # attacked - atakujacy
            if roll < 50:
                if self.get_power() <= attacked.get_power():
                    world.remove(self, attacked, True)
                else:
                    world.remove(attacked, self, False)
            else:
                print("antylopa uciekla")

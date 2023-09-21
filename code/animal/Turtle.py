from animal.Animal import Animal
import random

class Turtle(Animal):
    def __init__(self,x,y,age=0,power=2,init=1,photo="turtle.png",type='t'):
        super().__init__(x,y,age,power,init,photo,type)

    def action(self, world):
        roll = random.randint(0, 99)
        if roll < 25:
            super().action(world)

    def collision(self,attacked,world,number):
        if number == 1:
            # attacked atakowany
            if self.get_power()>=5:
                attacked.collision(self, world, 0)
            else:
                print("zolw odparl atak")
        else:
            # attacked - atakujacy
            if attacked.get_power()>=5:
                if self.get_power() <= attacked.get_power():
                    world.remove(self, attacked, True)
                else:
                    world.remove(attacked, self, False)
            else:
                print("zolw odparl atak")

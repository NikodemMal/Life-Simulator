from plants.Plant import Plant
from animal.Cyber_sheep import Cyber_sheep
from Ground import Ground

class Borscht(Plant):
    def __init__(self,x,y,age=0,power=10,init=0,photo="borscht.png",type='b'):
        super().__init__(x,y,age,power,init,photo,type)

    def collision(self,attacked,world,number):
            if number == 1:
                #attacked atakowany
                attacked.collision(self,world,0)
            else:
                #attacked - atakujacy
                if self.get_power() <= attacked.get_power():
                    if isinstance(attacked,Cyber_sheep):
                        print("cyber sheep zjadla barszcz")
                    else:
                        world.remove(attacked, self, False)
                    world.remove(self,attacked,True)
                else:
                    world.remove(attacked,self,False)

    def action(self, world):
        x = self.get_x()
        y = self.get_y()

        if x+1 < world.get_width():
            if not isinstance(world.get_board_org(y,x+1),Ground) and not isinstance(world.get_board_org(y,x+1),Cyber_sheep) and not isinstance(world.get_board_org(y,x+1),Plant):
                world.remove(world.get_board_org(y,x+1), self, False)
                print("barszcz zabija")
        if x-1 >= 0:
            if not isinstance(world.get_board_org(y,x-1),Ground) and not isinstance(world.get_board_org(y,x-1),Cyber_sheep) and not isinstance(world.get_board_org(y,x-1),Plant):
                world.remove(world.get_board_org(y, x-1), self, False)
                print("barszcz zabija")
        if y-1 >= 0:
            if not isinstance(world.get_board_org(y-1,x),Ground) and not isinstance(world.get_board_org(y-1,x),Cyber_sheep) and not isinstance(world.get_board_org(y-1,x),Plant):
                world.remove(world.get_board_org(y-1, x), self, False)
                print("barszcz zabija")
        if y+1 < world.get_height():
            if not isinstance(world.get_board_org(y+1,x),Ground) and not isinstance(world.get_board_org(y+1,x),Cyber_sheep) and not isinstance(world.get_board_org(y+1,x),Plant):
                world.remove(world.get_board_org(y+1, x), self, False)
                print("barszcz zabija")
        super().action(world)
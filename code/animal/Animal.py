from Organism import Organism
from Ground import Ground
import random

class Animal(Organism):

    def __init__(self, x,y,age,power,init,photo,type):
        super().__init__(x,y,age,power,init,photo,type)

    def action(self, world):
        for i in range(0,100):
            dir = random.randint(0,3)
            x_dir = 0
            y_dir = 0
            if dir == 0:
                x_dir = 1
                if self.get_x()+x_dir < world.get_width():
                    run = False
                    break
            elif dir == 1:
                x_dir = -1
                if self.get_x()+x_dir >=0:
                    run = False
                    break
            elif dir == 2:
                y_dir = 1
                if self.get_y()+y_dir < world.get_height():
                    run = False
                    break
            elif dir == 3:
                y_dir = -1
                if self.get_y()+y_dir >=0:
                    run = False
                    break
        if run == False:
            world.action_org(self,x_dir,y_dir)

    def scare_enemy(self,world):
        x = self.get_x()
        y = self.get_y()
        print("moc odstraszyla ",self.get_type())
        if x+1 < world.get_width() and isinstance(world.get_board_org(y,x+1),Ground):
            world.change_org(self,y,x+1)
        elif x-1 >= 0 and isinstance(world.get_board_org(y,x-1),Ground):
            world.change_org(self, y, x-1)
        elif y-1 >= 0 and isinstance(world.get_board_org(y-1,x),Ground):
            world.change_org(self, y-1, x)
        elif y+1 < world.get_height() and isinstance(world.get_board_org(y+1,x),Ground):
            world.change_org(self, y+1, x)
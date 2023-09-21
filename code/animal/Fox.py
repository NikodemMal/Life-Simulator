from animal.Animal import Animal
import random

class Fox(Animal):
    def __init__(self,x,y,age=0,power=3,init=7,photo="fox.png",type='f'):
        super().__init__(x,y,age,power,init,photo,type)

    def action(self, world):
        run = True
        for i in range(0,100):
            dir = random.randint(0,3)
            x_dir = 0
            y_dir = 0
            if dir == 0:
                x_dir = 1
                if self.get_x()+x_dir < world.get_width():
                    if world.get_board_org(self.get_y()+y_dir,self.get_x()+x_dir).get_power()<=self.get_power():
                        run = False
                        break
            elif dir == 1:
                x_dir = -1
                if self.get_x()+x_dir >=0:
                    if world.get_board_org(self.get_y() + y_dir, self.get_x() + x_dir).get_power() <= self.get_power():
                        run = False
                        break
            elif dir == 2:
                y_dir = 1
                if self.get_y()+y_dir < world.get_height():
                    if world.get_board_org(self.get_y() + y_dir, self.get_x() + x_dir).get_power() <= self.get_power():
                        run = False
                        break
            elif dir == 3:
                y_dir = -1
                if self.get_y()+y_dir >=0:
                    if world.get_board_org(self.get_y() + y_dir, self.get_x() + x_dir).get_power() <= self.get_power():
                        run = False
                        break
        if run == False:
            world.action_org(self,x_dir,y_dir)

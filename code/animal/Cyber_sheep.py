from animal.Animal import Animal

class Cyber_sheep(Animal):
    def __init__(self,x,y,age=0,power=11,init=4,photo="cyber_sheep.png",type='@'):
        super().__init__(x,y,age,power,init,photo,type)

    def action(self, world):
        lista = world.get_list()
        x_cyber = self.get_x()
        y_cyber = self.get_y()
        x = -10
        y = -10
        delta =-10
        x2 = -10
        y2 = -10
        delta2 = -10
        x_pos =-10
        y_pos =-10
        #szukanie pozycji najblizszego barszczu
        for it in lista:
            if it.get_type()=='b':
                if x<0:
                    x_pos=it.get_x()
                    y_pos=it.get_y()
                    x=it.get_x()-x_cyber
                    y=it.get_y()-y_cyber
                    if x<0:
                        x*=-1
                    if y<0:
                        y*=-1
                    delta=x+y
                else:
                    x2 = it.get_x() - x_cyber
                    y2 = it.get_y() - y_cyber
                    if x2 < 0:
                        x2 *= -1
                    if y2 < 0:
                        y2 *= -1
                    delta2 = x2 + y2
                    if delta2<delta:
                        x=x2
                        y=y2
                        delta=delta2
                        x_pos = it.get_x()
                        y_pos = it.get_y()
        if x_pos>=0:
            if x_pos!=x_cyber:
                if x_pos>x_cyber:
                    world.action_org(self, 1, 0)
                else:
                    world.action_org(self, -1, 0)
            else:
                if y_pos>y_cyber:
                    world.action_org(self, 0, 1)
                else:
                    world.action_org(self, 0, -1)
        else:
            super().action(world)

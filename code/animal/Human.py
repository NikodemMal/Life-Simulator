from animal.Animal import Animal

class Human(Animal):
    def __init__(self,x,y,age=0,power=5,init=4,photo="human.png",type='c'):
        super().__init__(x,y,age,power,init,photo,type)
    __ability_cooldown = 0

    def action(self,world,dir):
        x_dir = 0
        y_dir = 0
        run = False
        if dir == "right":
            x_dir = 1
            if self.get_x() + x_dir < world.get_width():
                run = True
        elif dir == "left":
            x_dir = -1
            if self.get_x() + x_dir >= 0:
                run = True
        elif dir == "down":
            y_dir = 1
            if self.get_y() + y_dir < world.get_height():
                run = True
        elif dir == "up":
            y_dir = -1
            if self.get_y() + y_dir >= 0:
                run = True
        elif dir == "ability":
            if self.__ability_cooldown == 0:
                print("wlaczanie mocy")
                self.__ability_cooldown = 10

        if run == True:
            world.action_org(self,x_dir,y_dir)

    def collision(self, attacked, world, number):

        if number == 1:
            # attacked atakowany
            if isinstance(self,Human) or isinstance(attacked,Human):
                if isinstance(self, Human) and self.__ability_cooldown >= 5 and isinstance(attacked,Animal):
                    attacked.scare_enemy(world)
                elif isinstance(attacked,Human) and attacked.__ability_cooldown >= 5 and isinstance(self,Animal):
                    self.scare_enemy(world)
                else:
                    attacked.collision(self, world, 0)
            else:
                attacked.collision(self, world, 0)
        else:
            # attacked - atakujacy
            if isinstance(self,Human) or isinstance(attacked,Human):
                if isinstance(self, Human) and self.__ability_cooldown >= 5 and isinstance(attacked,Animal):
                    attacked.scare_enemy(world)
                elif isinstance(attacked,Human) and attacked.__ability_cooldown >= 5 and isinstance(self,Animal):
                    self.scare_enemy(world)
                else:
                    attacked.collision(self, world, 0)
            else:
                if self.get_power() <= attacked.get_power():
                    world.remove(self, attacked, True)
                else:
                    world.remove(attacked, self, False)

    def update_ability(self):
        if self.__ability_cooldown > 0:
            self.__ability_cooldown-=1

    def get_ability(self):
        return self.__ability_cooldown

    def set_ability(self,a):
        self.__ability_cooldown=a
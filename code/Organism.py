
class Organism:

    def __init__(self,x,y,age,power,init,photo,type):
        self.__x = x
        self.__y = y
        self.__age = age
        self.__power = power
        self.__init = init
        self.__photo = photo
        self.__type = type

    def get_init(self):
        return self.__init

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self,a):
        self.__x = a

    def set_y(self,a):
        self.__y = a

    def get_age(self):
        return self.__age

    def Action(self, world):
        pass

    def get_photo(self):
        return self.__photo

    def get_type(self):
        return self.__type

    def update_age(self):
        self.__age+=1

    def get_age(self):
        return self.__age

    def get_power(self):
        return self.__power

    def set_power(self,a):
        self.__power = a

    def set_age(self,a):
        self.__age=a
    def set_init(self,a):
        self.__init=a

    def collision(self,attacked,world,number):
            if number == 1:
                #attacked atakowany
                attacked.collision(self,world,0)
            else:
                #attacked - atakujacy
                if self.__power <= attacked.__power:
                    world.remove(self,attacked,True)
                else:
                    world.remove(attacked,self,False)

    # types
    # Ground g

    # Wolf w
    # human h
    # sheep s
    # turtle t
    # antylope a
    # cyber_sheep @
    # fox f

    # Grass $
    # Dandelion d
    # Guarane %
    # Wolf_berries &
    # borscht b


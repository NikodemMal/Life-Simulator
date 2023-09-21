import sys
import os
import pygame
import random
from Button import Button
from Organism import Organism
from animal.Animal import Animal
from animal.Wolf import Wolf
from Ground import Ground
from animal.Human import Human
from animal.Sheep import Sheep
from animal.Turtle import Turtle
from animal.Antylope import Antylope
from animal.Cyber_sheep import Cyber_sheep
from animal.Fox import Fox
from plants.Plant import Plant
from plants.Grass import Grass
from plants.Dandelion import Dandelion
from plants.Guarane import Guarane
from plants.Wolf_berries import Wolf_berries
from plants.Borscht import Borscht


pygame.init()


class World:
    __organisms = []
    __board_org = None
    __size_of_image = 40
    __ground = Ground()
    __count_org = 11

    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        self.__screen = pygame.display.set_mode((1400, 1000))
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_board_org(self,y,x):
        return self.__board_org[y][x]

    def get_list(self):
        return self.__organisms

    def start_game(self):
        self.__screen.fill((0, 0, 0))
        self.ground_img = pygame.image.load('image/ground.png').convert_alpha()

        self.__board_org = [[self.__ground for i in range(self.__width)] for j in range(self.__height)]
        self.__board = [[Button() for i in range(0,self.__height)] for j in range(0,self.__width)]
        #ustawienie przyciskow org do dodania
        self.__choose_org = [Button() for i in range(0, self.__count_org)]
        self.__type_org = [self.__ground for i in range(self.__count_org)]
        self.__set_org_button()

        for i in range(0,self.__width):
            for j in range(0,self.__height):
                self.__board[i][j].set(i*self.__size_of_image+10+i*1,j*self.__size_of_image+10+j*1,self.ground_img)
                self.__board[i][j].draw(self.__screen)

        self.__add_atstart()
        pygame.display.flip()
        self.__game()


    def __add(self,new_organism):
        self.__board_org[new_organism.get_y()][new_organism.get_x()] = new_organism

        if len(self.__organisms) == 0:
            self.__organisms.insert(len(self.__organisms), new_organism)
        else:
            added = False
            for it in self.__organisms:
                if new_organism.get_init() > it.get_init():
                    self.__organisms.insert(self.__organisms.index(it), new_organism)
                    return
            if not added:
                self.__organisms.insert(len(self.__organisms), new_organism)

    def __game(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.__tur("down")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.__tur("up")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.__tur("left")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.__tur("right")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.__tur("None")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.__tur("ability")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.__save()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    self.__load_file()
                elif pygame.mouse.get_pressed()[0] == 1:
                    self.__mouse_click()




    def __tur(self,h_dir):
        for it in self.__organisms:
            it.update_age()

        for it in self.__organisms:
            if it.get_age() > 0:
                if isinstance(it,Human):
                    it.update_ability()
                    it.action(self,h_dir)
                else:
                    it.action(self)
        self.__draw()


    def action_org(self,organism,dir_x,dir_y):
        x = organism.get_x()
        y = organism.get_y()
        x2 = organism.get_x()+dir_x
        y2 = organism.get_y()+dir_y
        #self.board_org[y][x] = Ground()
        if isinstance(self.__board_org[y2][x2],Ground):
            organism.set_x(x2)
            organism.set_y(y2)
            self.__board_org[y2][x2] = organism
            self.__board_org[y][x] = self.__ground
        elif isinstance(self.__board_org[y2][x2],type(organism)):
            self.multiplication(organism)
        else:
            organism.collision(self.__board_org[y2][x2],self,1)

    def multiplication(self,organism):
        x=organism.get_x()
        y=organism.get_y()
        print("rozmnazanie",organism.get_type())
        if organism.get_age()>5:
            if x+1 < self.__width and isinstance(self.__board_org[y][x+1],Ground):
                self.__board_org[y][x + 1] = type(organism)(x+1,y)
                self.__add(self.__board_org[y][x + 1])
            elif x-1 >= 0 and isinstance(self.__board_org[y][x-1],Ground):
                self.__board_org[y][x - 1] = type(organism)(x-1,y)
                self.__add(self.__board_org[y][x - 1])
            elif y+1 < self.__height and isinstance(self.__board_org[y+1][x],Ground):
                self.__board_org[y+1][x] = type(organism)(x,y+1)
                self.__add(self.__board_org[y+1][x])
            elif y-1 >= 0 and isinstance(self.__board_org[y-1][x],Ground):
                self.__board_org[y-1][x] = type(organism)(x,y-1)
                self.__add(self.__board_org[y-1][x])

    def remove(self,to_remove,organism,change):
        x = to_remove.get_x()
        y = to_remove.get_y()
        print(organism.get_type(),"zabija",to_remove.get_type())
        if change:
            x2 = organism.get_x()
            y2 = organism.get_y()
            self.__board_org[y][x] = organism
            organism.set_x(x)
            organism.set_y(y)
            self.__board_org[y2][x2] = self.__ground
        else:
            self.__board_org[y][x] = self.__ground

        self.__organisms.remove(to_remove)

    def __add_atstart(self):
        run = True
        while run:
            y_pos = random.randint(0, self.__height - 1)
            x_pos = random.randint(0, self.__width - 1)
            if self.__board[x_pos][y_pos].get_image() == self.ground_img:
                run = False
                self.__add(Human(x_pos, y_pos))
                self.__board[x_pos][y_pos].set_image(self.__board_org[y_pos][x_pos].get_photo())
                self.__board[x_pos][y_pos].draw(self.__screen)

        for i in range(0, 44):
            run = True
            while run:
                y_pos = random.randint(0, self.__height - 1)
                x_pos = random.randint(0, self.__width - 1)
                if self.__board[x_pos][y_pos].get_image() == self.ground_img:
                    run = False
                    if i < 4:
                        self.__add(Wolf(x_pos, y_pos))
                    elif i < 8:
                        self.__add(Sheep(x_pos, y_pos))
                    elif i < 12:
                        self.__add(Turtle(x_pos, y_pos))
                    elif i < 16:
                        self.__add(Antylope(x_pos, y_pos))
                    elif i < 20:
                        self.__add(Cyber_sheep(x_pos, y_pos))
                    elif i < 24:
                        self.__add(Dandelion(x_pos, y_pos))
                    elif i < 28:
                        self.__add(Guarane(x_pos, y_pos))
                    elif i < 32:
                        self.__add(Wolf_berries(x_pos, y_pos))
                    elif i < 36:
                        self.__add(Borscht(x_pos, y_pos))
                    elif i < 40:
                        self.__add(Fox(x_pos, y_pos))
                    else:
                        self.__add(Grass(x_pos, y_pos))

                    self.__board[x_pos][y_pos].set_image(self.__board_org[y_pos][x_pos].get_photo())
                    self.__board[x_pos][y_pos].draw(self.__screen)

    def change_org(self,organism,to_y2,to_x2):
        x = organism.get_x()
        y = organism.get_y()
        self.__board_org[to_y2][to_x2] = self.__board_org[y][x]
        self.__board_org[y][x] = self.__ground
        organism.set_x(to_x2)
        organism.set_y(to_y2)

    def __mouse_click(self):
        pos_x=-10

        for i in range(0, self.__height):
            for j in range(0, self.__width):
                if self.__board[j][i].draw(self.__screen):
                    pos_x=j
                    pos_y=i


        if pos_x>=0 and isinstance(self.__board_org[pos_y][pos_x],Ground):
            self.__screen.fill((0, 0, 0))
            for i in range(0, self.__count_org):
                self.__choose_org[i].draw(self.__screen)
            pygame.display.flip()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif pygame.mouse.get_pressed()[0] == 1:
                        for i in range(0, self.__count_org):
                            if self.__choose_org[i].draw(self.__screen):
                                x = i
                                self.__add(type(self.__type_org[x])(pos_x,pos_y))
                                run=False
                                self.__screen.fill((0, 0, 0))
                                self.__draw()
                                self.__game()
        else:
            self.__draw()
            self.__game()


    def __draw(self):
        self.__screen.fill((0, 0, 0))
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                self.__board[j][i].set_image(self.__board_org[i][j].get_photo())
                self.__board[j][i].draw(self.__screen)

        pygame.display.flip()

    def __save(self):
        print("zapisywanie")
        file = open("save/save.txt","w")
        file.write(str(self.__width) + " " + str(self.__height) + " " + str(len(self.__organisms)) + "\n")
        for it in self.__organisms:
            if isinstance(it,Human):
                file.write(it.get_type()+" "+str(it.get_y())+" "+str(it.get_x())+" "+str(it.get_age())+" "+str(it.get_power())+" "+str(it.get_init())+" "+str(it.get_ability())+ '\n')
            else:
                file.write(it.get_type()+" "+str(it.get_y())+" "+str(it.get_x())+" "+str(it.get_age())+" "+str(it.get_power())+" "+str(it.get_init())+ '\n')
        file.close()

    def __load_file(self):
        if os.path.isfile("save/save.txt"):
            print("wczytywanie")
            file = open("save/save.txt","r")
            self.__organisms.clear()
            read = file.readline()
            read = read.split(" ")
            self.__width=int(read[0])
            self.__height=int(read[1])
            count_org=int(read[2])
            self.__screen.fill((0, 0, 0))
            self.__board_org = [[self.__ground for i in range(self.__width)] for j in range(self.__height)]
            self.__board = [[Button() for i in range(0, self.__height)] for j in range(0, self.__width)]

            for i in range(0, self.__width):
                for j in range(0, self.__height):
                    self.__board[i][j].set(i * self.__size_of_image + 10 + i * 1, j * self.__size_of_image + 10 + j * 1,self.ground_img)
                    self.__board[i][j].draw(self.__screen)

            for i in range(0,count_org):
                read = file.readline()
                read = read.split(" ")

                type=read[0]
                x_pos=int(read[2])
                y_pos=int(read[1])
                if read[0]=='w':
                    self.__add(Wolf(x_pos, y_pos))
                elif read[0]=='s':
                    self.__add(Sheep(x_pos, y_pos))
                elif read[0]=='t':
                    self.__add(Turtle(x_pos, y_pos))
                elif read[0]=='a':
                    self.__add(Antylope(x_pos, y_pos))
                elif read[0]=='@':
                    self.__add(Cyber_sheep(x_pos, y_pos))
                elif read[0]=='d':
                    self.__add(Dandelion(x_pos, y_pos))
                elif read[0]=='%':
                    self.__add(Guarane(x_pos, y_pos))
                elif read[0]=='&':
                    self.__add(Wolf_berries(x_pos, y_pos))
                elif read[0]=='b':
                    self.__add(Borscht(x_pos, y_pos))
                elif read[0]=='f':
                    self.__add(Fox(x_pos, y_pos))
                elif read[0]=='c':
                    self.__add(Human(x_pos, y_pos))
                else:
                    self.__add(Grass(x_pos, y_pos))

                self.__board_org[y_pos][x_pos].set_age(int(read[3]))
                self.__board_org[y_pos][x_pos].set_power(int(read[4]))
                self.__board_org[y_pos][x_pos].set_init(int(read[5]))
                if isinstance(self.__board_org[y_pos][x_pos],Human):
                    self.__board_org[y_pos][x_pos].set_ability(int(read[6]))

                self.__board[x_pos][y_pos].set_image(self.__board_org[y_pos][x_pos].get_photo())
                self.__board[x_pos][y_pos].draw(self.__screen)
            file.close()
            pygame.display.flip()
            self.__game()
        else:
            print("plik nie istnieje")

    def __set_org_button(self):
        self.__type_org[0] = Wolf(1, 1)
        self.__type_org[1] = Sheep(1, 1)
        self.__type_org[2] = Turtle(1, 1)
        self.__type_org[3] = Antylope(1, 1)
        self.__type_org[4] = Cyber_sheep(1, 1)
        self.__type_org[5] = Fox(1, 1)
        self.__type_org[6] = Grass(1, 1)
        self.__type_org[7] = Dandelion(1, 1)
        self.__type_org[8] = Guarane(1, 1)
        self.__type_org[9] = Wolf_berries(1, 1)
        self.__type_org[10] = Borscht(1, 1)
        for i in range(0, self.__count_org):
            name = self.__type_org[i].get_photo()
            self.__choose_org[i].set(i * self.__size_of_image + 50 + i * 1, 500,pygame.image.load('image/' + name).convert_alpha())

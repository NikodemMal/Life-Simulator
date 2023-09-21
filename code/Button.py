import pygame
pygame.init()

class Button():

    def set(self,x,y,image):
        self.__image = image
        self.__rect = self.__image.get_rect()
        self.__rect.topleft = (x,y)
        self.__clicked = False

    def set_image(self,image):
        self.__image = pygame.image.load("image/"+image).convert_alpha()
        a = self.__rect.topleft
        self.__rect = self.__image.get_rect()
        self.__rect.topleft = a

    def draw(self,screen):
        pos = pygame.mouse.get_pos()
        czy = False
        if self.__rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.__clicked = True
                czy = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.__clicked = False

        screen.blit(self.__image,(self.__rect.x,self.__rect.y))
        if czy:
            return czy

    def get_image(self):
        return self.__image

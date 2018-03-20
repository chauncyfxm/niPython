import pygame
from plant_sprites import *

class Hero(GameSprite):

    def __init__(self, *arge):

        super().__init__(arge[0])
        self.lock = False

    def update(self, *arge):
        # print("123")
        #self.lock = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("按下！")
                #self.lock = True

            #key
                if self.lock:
                    if event.key == pygame.K_d:
                        self.rect.x += 3

                    elif event.key == pygame.K_a:
                        self.rect.x -= 3

                    elif event.key == pygame.K_w:
                        self.rect.y -= 3

                    elif event.key == pygame.K_s:
                        self.rect.y += 3



                    #出界
                    elif self.rect.x <= 0:
                        self.rect.x = 0

                    elif self.rect.x >= SCREEN_RECT.width:
                        self.rect.x = SCREEN_RECT.width

                    elif self.rect.y <= 0:
                        self.rect.y = 0

                    elif self.rect.y >= SCREEN_RECT.height:
                        self.rect.y = SCREEN_RECT.height


'''

class Hero(GameSprite):
    def __init__(self,*arge):
        
        super().__init__(arge[0])
        self.speed1 = 0
        self.speed2 = 0
    def update(self,*arge):
        self.rect.x += self.speed1
        self.rect.y += self.speed2
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.speed1 = 2

                elif event.key == pygame.K_LEFT:
                    self.speed1 = -2

                elif event.key == pygame.K_UP:
                    self.speed2 = -2

                elif event.key == pygame.K_DOWN:
                    self.speed2 = 2

                elif self.rect.x <= 0:
                    self.rect.x = 0
                     
                elif self.rect.x >= SCREEN_RECT.height:
                    self.rect.x = SCREEN_RECT.height
            else:
                self.speed1 = 0
                self.speed2 = 0


'''
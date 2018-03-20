import pygame
from plane_sprites import *


pygame.init()


bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
hero_rect = pygame.Rect(100,500,130,130)

enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png",2)
enemy2.rect.x = 200


print("坐标原点 %d %d"% (hero_rect.x,hero_rect.y))
print('英雄大小 %d %d'% (hero_rect.width,hero_rect.height))

clock = pygame.time.Clock()
screan = pygame.display.set_mode((480,700),1)
while True: 
    screan.blit(bg,(0,0))
    screan.blit(hero,hero_rect)
    clock.tick(60)
    hero_rect.y -=1
    if hero_rect.y <=0:
        hero_rect.y = 700
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏、、")
            pygame.quit()
            exit()


    enemy_group = pygame.sprite.Group(enemy1,enemy2)

    enemy_group.update()

    enemy_group.draw(screan)

    pygame.display.update()


    

pygame.quit()


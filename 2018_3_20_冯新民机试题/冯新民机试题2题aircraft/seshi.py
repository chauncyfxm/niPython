import pygame


pygame.init()

clock = pygame.time.Clock()
COUNT = pygame.USEREVENT
pygame.time.set_timer	(COUNT,1)

while True:
	clock.tick(1)
	print(COUNT)

a = pygame.key.get_pressed()

print(a)
print(pygame.K_UP)


pygame.quit()
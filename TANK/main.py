import pygame
from persone import Hero
pygame.init()
clock = pygame.time.Clock()
WIDTH = 640
HEIGHT = 480
RUN = True
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
tank = Hero(WINDOW)
while RUN:
    pygame.display.update()
    WINDOW.fill((0,0,0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tank.l_pos = True
            if event.key == pygame.K_RIGHT:
                tank.r_pos = True
            if event.key == pygame.K_UP:
                tank.u_pos = True
            if event.key == pygame.K_DOWN:
                tank.d_pos = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                tank.l_pos = False
            if event.key == pygame.K_RIGHT:
                tank.r_pos = False
            if event.key == pygame.K_UP:
                tank.u_pos = False
            if event.key == pygame.K_DOWN:
                tank.d_pos = False
    
    tank.draw()
    tank.update_position()

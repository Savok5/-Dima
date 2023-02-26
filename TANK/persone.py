import pygame


class Hero():
    def __init__(self, window):
        self.window = window
        self.image_up = pygame.image.load('picture/tank_up.png')
        self.image_left = pygame.image.load('picture/tank_left.png')
        self.image_right = pygame.image.load('picture/tank_right .png')
        self.image_down = pygame.image.load('picture/tank_down.png')
        self.image =  self.image_up
        self.rect = self.image.get_rect()
        self.screen_rect = window.get_rect()
        self.rect.x = 640/2-25
        self.rect.y = 480/2-25
        self.l_pos = False
        self.r_pos = False
        self.u_pos = False
        self.d_pos = False

    def draw(self):
        self.window.blit(self.image,self.rect)
    
    def update_position(self):
        if self.l_pos==True and self.rect.x>0:
            self.rect.x -= 3
            self.image = self.image_left
        elif self.r_pos==True and self.rect.x<590:
            self.rect.x += 3
            self.image = self.image_right
        elif self.u_pos==True and self.rect.y>0:
            self.rect.y -= 3
            self.image = self.image_up
        elif self.d_pos==True and self.rect.y<430:
            self.rect.y += 3
            self.image = self.image_down
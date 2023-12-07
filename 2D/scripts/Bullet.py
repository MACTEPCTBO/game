import pygame.sprite

from setting import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('texture/bullet/bullet_0.png')
        self.rect = self.image.get_rect(center=(x,y))

        self.mx,self.my = pygame.mouse.get_pos()
        self.ax,self.ay = 0,0

        self.x,self.y = x,y

        if self.rect.x + 10 < self.mx:
            self.rect.x += cell
            self.ax = 1
        elif self.rect.x - 10 > self.mx:
            self.rect.x -= cell
            self.ax = -1
        else:
            self.ax = 0

        if self.rect.y + 10 < self.my:
            self.rect.y += cell
            self.ay = 1
        elif self.rect.y - 10 > self.my:
            self.rect.y -= cell
            self.ay = -1
        else:
            self.ay = 0

        self.distance = 0

    def update(self):
        self.rect.x += self.ax
        self.rect.y += self.ay

        self.distance += 1
        if self.distance >= 55:
            self.kill()

        hits = pygame.sprite.groupcollide(bot_,bullet_,False,True)
        for hit in hits:
            hit.HP -= 1

        screen.blit(self.image,self.rect)
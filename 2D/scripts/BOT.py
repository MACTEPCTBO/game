import random

import pygame.sprite

from setting import *

class Bot(pygame.sprite.Sprite):
    def __init__(self,x,y,player):
        super().__init__()
        self.image = pygame.image.load('texture/bot/bot_0.png')
        self.rect = self.image.get_rect(center=(x,y))

        self.HP = 10
        self.speed = 1

        self.player = player


    def update(self):
        if self.HP <= 0:
            bot_.add(Bot(random.randint(0, WIDTH // cell * cell), random.randint(0, HEIGHT // cell * cell),
                     self.player))
            self.kill()

        if self.player.rect.x > self.rect.x:
            self.rect.x += self.speed
        elif self.player.rect.x < self.rect.x:
            self.rect.x -= self.speed

        if self.player.rect.y > self.rect.y:
            self.rect.y += self.speed
        elif self.player.rect.y < self.rect.y:
            self.rect.y -= self.speed

        if self.rect.x == self.player.rect.x and self.rect.y == self.player.rect.y:
            self.kill()
            self.player.life = False




        screen.blit(self.image,self.rect)

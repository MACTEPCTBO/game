import pygame,random

WIDTH,HEIGHT,cell,FPS = 700,700,10,60
screen,time = pygame.display.set_mode((WIDTH,HEIGHT)),pygame.time.Clock()

bot_ = pygame.sprite.Group()
bullet_ = pygame.sprite.Group()
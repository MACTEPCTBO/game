import random

from setting import *
from scripts.PLAYER import Player
from scripts.BOT import Bot

player = Player()

for i in range(10):
    bot = Bot(random.randint(0, WIDTH // cell * cell), random.randint(0, HEIGHT // cell * cell), player)
    bot_.add(bot)

while 1:
    screen.fill((100,100,100))
    k = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    bullet_.update()
    bot_.update()
    player.update(k)

    pygame.display.flip()
    time.tick(FPS)
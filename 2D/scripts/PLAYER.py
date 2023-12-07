from setting import *
from scripts.Bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self,x=WIDTH//2,y=HEIGHT//2):
        super().__init__()

        self.image = pygame.image.load('texture/player/player.png')
        self.rect = self.image.get_rect(center=(x,y))

        self.speed = 1

        self.life = True
        self.fire_time = 0
        self.fire = True

    def update(self,k):
        if self.life:
            if self.fire_time >= 10:
                self.fire = True
                self.fire_time = 0

            m = pygame.mouse.get_pressed()
            if k[pygame.K_a] and self.rect.x - self.speed >= 0:
                self.rect.x -= self.speed
            elif k[pygame.K_d] and self.rect.x + self.speed <= WIDTH:
                self.rect.x += self.speed

            if k[pygame.K_w] and self.rect.y - self.speed >= 0:
                self.rect.y -= self.speed
            elif k[pygame.K_s] and self.rect.y + self.speed * 10 <= HEIGHT:
                self.rect.y += self.speed

            if m[0] and self.fire:
                self.fire = False
                bullet_.add(Bullet(self.rect.x + cell // 2,self.rect.y + cell ))

            self.fire_time += 1



            pygame.draw.circle(screen,'black',(self.rect.x+cell,self.rect.y+cell),100,1)
            screen.blit(self.image,self.rect)
        else:
            self.kill()


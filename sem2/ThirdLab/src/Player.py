from Entity import Entity
from settings import *
from FirstGun import FirstGun
from BulletManager import BulletManager

class Player(Entity):
    
    def __init__(self, group,bm:BulletManager):
        super().__init__(group,bm=bm)
        self.image = pygame.surface.Surface((200,200))
        self.image = pygame.transform.scale(self.image,(WIDTH_OF_PLATE,HEIGHT_OF_PLATE))
        self.rect = self.image.get_rect()
        self.shooting_direction = Directions.UP
        self.setup()
        
    def setup(self):
        self.direction = 0
        self.rect.centerx = WIDTH/2 - WIDTH_OF_PLATE/2
        self.rect.centery = HEIGHT - HEIGHT_OF_PLATE/2
        self.temp_rect = self.rect
        self.shooting = False
        self.gun = FirstGun(self.bm,self.shooting_direction)
        self.delay = DELAY_BETWEEN_SHOTS

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.shooting = keys[pygame.K_SPACE]
            
    def move(self,dt):
        if self.rect.left>0 and self.direction == -1:
            self.temp_rect.centerx += self.direction * SPEED_OF_PLATE * dt
            self.rect.centerx = self.temp_rect.centerx
        elif self.rect.right<WIDTH and self.direction == 1:
            self.temp_rect.centerx += self.direction * SPEED_OF_PLATE * dt
            self.rect.centerx = self.temp_rect.centerx
        
    def shoot(self):
        if self.shooting and self.delay >= DELAY_BETWEEN_SHOTS:
            self.gun.shoot(self.rect.center)
            self.delay = 0
            
    
    def update(self,dt):
        self.delay +=dt
        self.input()
        self.move(dt)
        self.shoot()
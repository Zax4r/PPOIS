from Enemy import Enemy
from settings import *
from BulletManager import BulletManager
from FirstGun import FirstGun
import random

class FirstEnemy(Enemy):
    
    def __init__(self, *groups, bm:BulletManager,pos,direction):
        super().__init__(*groups, bm=bm,pos=pos,direction=direction)     
        self.image = pygame.surface.Surface((200,200))
        self.image = pygame.transform.scale(self.image,(WIDTH_OF_FIRST_ENEMY,HEIGHT_OF_FIRST_ENEMY))
        self.rect = self.image.get_rect()
        self.setup(pos,direction)
        
    def setup(self,pos,direction):
        self.direction = direction
        self.rect.center = pos
        self.temp_rect = self.rect
        self.shooting = False
        self.gun = FirstGun(self.bm,self.shooting_direction)
        self.delay = DELAY_BETWEEN_SHOTS

    def input(self):
        self.shooting = random.randint(1,1000)
        if self.rect.left <= 0:
            self.direction = 1
        if self.rect.right >= WIDTH:
            self.direction = -1    
        
            
    def move(self,dt):
        self.temp_rect.centerx += self.direction * SPEED_OF_FIRST_ENEMY * dt
        self.rect.centerx = self.temp_rect.centerx
        
    def shoot(self):
        if self.shooting>100 and self.delay >= DELAY_BETWEEN_SHOTS:
            self.gun.shoot(self.rect.center)
            self.delay = 0
            
    def update(self,dt):
        self.delay +=dt
        self.input()
        self.move(dt)
        self.shoot()
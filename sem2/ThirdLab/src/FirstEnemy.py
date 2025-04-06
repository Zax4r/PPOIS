from EnemyI import EnemyI
from settings import *
from BulletManager import BulletManager
from FirstGun import FirstGun

class FirstEnemy(EnemyI):
    
    def __init__(self, *groups, bm:BulletManager,pos):
        super().__init__(*groups, bm=bm,hp = HP_OF_FIRST_ENEMY)     
        
        self.image = pygame.surface.Surface((200,200))
        self.image = pygame.transform.scale(self.image,(WIDTH_OF_ENEMY,HEIGHT_OF_ENEMY))
        self.rect = self.image.get_rect(topleft = pos)
        self.centerx = self.rect.centerx
        
        self.gun = FirstGun(self.bm,self.aim)            
            
    def move(self,dt,direction_of_moving):
        self.centerx += direction_of_moving * SPEED_OF_ENEMY * dt
        self.rect.centerx = self.centerx
        
    def shoot(self):
        self.gun.shoot(self.rect.center)
    
    def update(self,dt,direction_of_moving):
        self.move(dt,direction_of_moving)
from settings import *
from Gun import Gun
from Bullet import Bullet
from BulletManager import BulletManager

class FirstGun(Gun):
    
    def __init__(self,bm:BulletManager,direction:Directions):
        super().__init__(bm,direction)
        
        
    def shoot(self,pos:pygame.Vector2):
        self.bm.add_bullet(Bullet(pos,self.direction))
    
    
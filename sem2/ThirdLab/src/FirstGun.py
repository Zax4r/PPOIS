from settings import *
from Gun import Gun
from Bullet import Bullet
from BulletManager import BulletManager

class FirstGun(Gun):
    
    def __init__(self,bm:BulletManager,direction:Directions):
        super().__init__(bm,direction)
        self.style_of_gun = Directions.UP.value
        self.res_direction = pygame.Vector2(self.style_of_gun.x,self.direction.y)
        
    def shoot(self,pos:pygame.Vector2): 
        self.bm.add_bullet(Bullet(pos,self.res_direction))
    
    
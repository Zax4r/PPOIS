from .Gun import *
from .Bullets.BouncingBullet import BouncingBullet


class SecondGun(Gun):
    
    def __init__(self,bm:BulletManagerI,direction:Directions,data):
        self.data = data
        super().__init__(bm,direction)
        self.styles_of_gun = [Directions.UPRIGHT45.value,Directions.UPLEFT45.value]
        self.res_directions = [pygame.Vector2(style_of_gun.x,self.direction.y).normalize() for style_of_gun in self.styles_of_gun]
        
    def shoot(self,pos:pygame.Vector2): 
        for direction in self.res_directions:
            self.bm.add_bullet(BouncingBullet(pos,direction.copy(),self.data))
    
    
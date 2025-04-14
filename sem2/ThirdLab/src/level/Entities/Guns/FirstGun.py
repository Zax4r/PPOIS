from .Gun import *
from .Bullets.SimpleBullet import SimpleBullet

class FirstGun(Gun):
    
    def __init__(self,bm:BulletManagerI,direction:Directions,data):
        self.data = data
        super().__init__(bm,direction)
        self.styles_of_gun = [Directions.UP.value]
        self.res_directions = [pygame.Vector2(style_of_gun.x,self.direction.y).normalize() for style_of_gun in self.styles_of_gun]
        
    def shoot(self,pos:pygame.Vector2): 
        for direction in self.res_directions:
            self.bm.add_bullet(SimpleBullet(pos,direction,self.data))
    
    
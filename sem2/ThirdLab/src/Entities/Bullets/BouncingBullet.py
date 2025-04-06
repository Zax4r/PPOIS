from .Bullet import Bullet
from .settings import *

class BouncingBullet(Bullet):
    
    def __init__(self, pos, direction):
        super().__init__(pos, direction)
        self.dmg = DAMAGE_BOUNCING_BULLET
        
    def update_direction(self):
        if self.direction.x >0 and self.rect.right>=WIDTH:
            self.direction.x = -1 * abs(self.direction.x)
        elif self.direction.x <0 and self.rect.left<=0:
            self.direction.x = abs(self.direction.x)
    
        
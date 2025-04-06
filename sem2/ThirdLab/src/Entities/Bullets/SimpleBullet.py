from .Bullet import Bullet
from .settings import *
class SimpleBullet(Bullet):
    
    def __init__(self, pos, direction):
        super().__init__(pos, direction)
        self.dmg = DAMAGE_SIMPLE_BULLET
        
    def update_direction(self):
        self.direction = self.direction
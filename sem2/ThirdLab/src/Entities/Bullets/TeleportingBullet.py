from .Bullet import Bullet
from .settings import *

class TeleportingBullet(Bullet):
    
    def __init__(self, pos, direction):
        super().__init__(pos, direction)
        self.dmg = DAMAGE_TELEPORTING_BULLET
        
        
    def update_direction(self):
        self.centerx %= WIDTH
    
        
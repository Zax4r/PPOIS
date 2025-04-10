from .Bullet import Bullet

class TeleportingBullet(Bullet):
    
    def __init__(self, pos, direction,data):
        super().__init__(pos, direction,data=data,path="./graphics/bullets/teleporting/1.png")
        self.dmg = 1
        
        
    def update_direction(self):
        self.centerx %= self.data['WIDTH']
    
        
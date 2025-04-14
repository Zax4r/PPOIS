from .Bullet import Bullet

class BouncingBullet(Bullet):
    
    def __init__(self, pos, direction,data):
        super().__init__(pos, direction,data=data,path="./graphics/bullets/bouncing/1.png")
        self.dmg = 1
        
    def update_direction(self):
        if self.direction.x >0 and self.rect.right>=self.data['WIDTH']:
            self.direction.x = -1 * abs(self.direction.x)
        elif self.direction.x <0 and self.rect.left<=0:
            self.direction.x = abs(self.direction.x)
    
        
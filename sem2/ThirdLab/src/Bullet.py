from settings import *

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self,pos,direction:Directions):
        super().__init__()
        self.image = pygame.surface.Surface((WIDTH_OF_BULLET,HEIGHT_OF_BULLET))
        self.rect = self.image.get_rect(center = pos)
        self.direction = direction
        self.temp_rect = self.rect
        
    def move(self,dt):
        self.temp_rect.center += self.direction * VELOCITY_OF_BULLET * dt
        self.rect.center = self.temp_rect.center
        
    def update(self,dt):
        self.move(dt)
    
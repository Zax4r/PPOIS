from .settings import *
import abc
class Bullet(pygame.sprite.Sprite,abc.ABC):
    
    def __init__(self,pos,direction:Directions):
        super().__init__()
        self.image = pygame.surface.Surface((WIDTH_OF_BULLET,HEIGHT_OF_BULLET))
        self._rect = self.image.get_rect(center = pos)
        self.direction = direction
        self.centerx,self.centery = self._rect.center
        
    def move(self,dt):
        self.centerx += self.direction.x * VELOCITY_OF_BULLET * dt
        self.centery += self.direction.y * VELOCITY_OF_BULLET * dt
        self._rect.center = self.centerx,self.centery
    
    @abc.abstractmethod
    def update_direction(self):
        pass
    
    def update(self,dt):
        self.update_direction()
        self.move(dt)
    
    @property
    def getrecty(self):
        return self._rect.centery

    @property
    def rect(self):
        return self._rect
from Directions import Directions
import pygame
import abc
class Bullet(pygame.sprite.Sprite,abc.ABC):
    
    def __init__(self,pos,direction:Directions,data,path):
        super().__init__()
        self.data = data
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,(data['bullet']['WIDTH_OF_BULLET'],data['bullet']['HEIGHT_OF_BULLET']))
        self._rect = self.image.get_rect(center = pos)
        self.direction = direction
        self.centerx,self.centery = self._rect.center
        
    def move(self,dt):
        self.centerx += self.direction.x * self.data['bullet']['VELOCITY_OF_BULLET'] * dt
        self.centery += self.direction.y * self.data['bullet']['VELOCITY_OF_BULLET'] * dt
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
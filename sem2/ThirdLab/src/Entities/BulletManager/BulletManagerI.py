import abc
import pygame

class BulletManagerI(abc.ABC,pygame.sprite.Group):
    
    def __init__(self, *sprites):
        super().__init__(*sprites)
    
    @abc.abstractmethod
    def add_bullet(self,bullet):
        pass
    
    @abc.abstractmethod        
    def update(self,dt):
        pass
    
    @abc.abstractmethod
    def delete_exited(self):
        pass
    
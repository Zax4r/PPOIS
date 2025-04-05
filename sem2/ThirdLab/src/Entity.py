import pygame
import abc

class Entity(pygame.sprite.Sprite,abc.ABC):
    
    def __init__(self, *groups):
        super().__init__(*groups)
    
    @abc.abstractmethod
    def input (self):
        pass
    
    @abc.abstractmethod
    def move(self,dt):
        pass
    
    @abc.abstractmethod
    def shoot(self):
        pass
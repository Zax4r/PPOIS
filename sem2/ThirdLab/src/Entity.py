import pygame
import abc
from BulletManager import BulletManager

class Entity(pygame.sprite.Sprite,abc.ABC):
    
    def __init__(self, *groups,bm: BulletManager):
        super().__init__(*groups)
        self.bm = bm
    
    @abc.abstractmethod
    def input (self):
        pass
    
    @abc.abstractmethod
    def move(self,dt):
        pass
    
    @abc.abstractmethod
    def shoot(self):
        pass
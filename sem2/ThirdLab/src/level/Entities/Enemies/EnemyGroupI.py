import pygame
import abc

class EnemyGroupI(abc.ABC,pygame.sprite.Group):
    
    @abc.abstractmethod
    def load(self,enemies):
        pass
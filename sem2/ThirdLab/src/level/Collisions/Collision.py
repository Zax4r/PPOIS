import abc
import pygame

class Collision(abc.ABC):
    
    @abc.abstractmethod
    def collision(self,first:pygame.sprite.Group,second:pygame.sprite.Group):
        pass

    @abc.abstractmethod
    def check_collision(self,first:pygame.sprite.Group,second:pygame.sprite.Group):
        pass
    
    @abc.abstractmethod
    def work_with_collision(self,sprite1:pygame.sprite.Sprite,sprite2:pygame.sprite.Sprite,first:pygame.sprite.Group,second:pygame.sprite.Group):
        pass
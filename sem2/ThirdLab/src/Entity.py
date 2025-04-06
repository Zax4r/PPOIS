import pygame
from settings import *
from BulletManagerI import BulletManagerI
from MovingI import MovingI
import abc

class Entity(pygame.sprite.Sprite,MovingI):
    
    def __init__(self, *groups,bm:BulletManagerI,hp):
        pygame.sprite.Sprite.__init__(self,*groups)
        self.bm = bm
        self.hp = hp
        self.rect:pygame.rect.Rect
        
    @property
    def getrect(self):
        return self.rect
    
    def update_hp(self,dmg):
        if self.hp <= dmg:
            return False
        self.hp -= dmg   
        return True
    
        
    
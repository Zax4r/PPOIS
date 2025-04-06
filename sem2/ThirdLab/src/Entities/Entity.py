import pygame
from .BulletManager.BulletManagerI import BulletManagerI
from .MovingI import MovingI
from .Guns.FirstGun import FirstGun
from .Guns.SecondGun import SecondGun
from .Guns.ThirdGun import ThirdGun
import abc

class Entity(pygame.sprite.Sprite,MovingI):
    
    def __init__(self, *groups,bm:BulletManagerI,hp:int,img:pygame.surface.Surface):
        pygame.sprite.Sprite.__init__(self,*groups)
        self.bm = bm
        self.hp = hp
        self.image = img
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect()
        
    @property
    def getrect(self):
        return self.rect
    
    def update_hp(self,dmg):
        if self.hp <= dmg:
            return False
        self.hp -= dmg   
        return True
    
        
    
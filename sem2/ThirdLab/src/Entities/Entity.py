import pygame
from .BulletManager.BulletManagerI import BulletManagerI
from .MovingI import MovingI
from .Guns.FirstGun import FirstGun
from .Guns.SecondGun import SecondGun
from .Guns.ThirdGun import ThirdGun

class Entity(pygame.sprite.Sprite,MovingI):
    
    def __init__(self, *groups,bm:BulletManagerI,hp:int,img:pygame.surface.Surface):
        pygame.sprite.Sprite.__init__(self,*groups)
        self.bm = bm
        self.hp = hp
        self.image = img
        self.score = 0
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()
        
    @property
    def getrect(self):
        return self.rect
    
    def update_hp(self,dmg):
        self.hp -= dmg   
    
    def get_status(self):
        return self.hp > 0
    
        
    
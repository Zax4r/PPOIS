from ..Entity import Entity
from .InputI import InputI
from ..Guns.FirstGun import FirstGun
from ..Guns.SecondGun import SecondGun
from ..Guns.ThirdGun import ThirdGun
from Directions import Directions
import pygame

class PlayerI(Entity,InputI):
    def __init__(self, *groups,bm,hp,img):
        self.available_guns = {1:FirstGun,2:SecondGun,3:ThirdGun}
        img = pygame.transform.scale(img,(self.data['player']['WIDTH_OF_PLAYER'],self.data['player']['HEIGHT_OF_PLAYER']))
        super().__init__(*groups,bm=bm,hp=hp,img=img)
        self.aim = Directions.UP
    
    def update_image(self, img):
        img = pygame.transform.scale(img,(self.data['player']['WIDTH_OF_PLAYER'],self.data['player']['HEIGHT_OF_PLAYER']))
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.mask = self.mask.to_surface()
        self.mask.set_colorkey('black')
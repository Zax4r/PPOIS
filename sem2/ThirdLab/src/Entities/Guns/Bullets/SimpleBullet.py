from .Bullet import Bullet
import pygame
class SimpleBullet(Bullet):
    
    def __init__(self, pos, direction,data):
        super().__init__(pos, direction,data=data,path="./graphics/bullets/simple/1.png")
        self.dmg = 1
        
    def update_direction(self):
        self.direction = self.direction
import pygame
from .settings import *

class Bonus(pygame.sprite.Sprite):
    
    def __init__(self, *groups,pos):
        super().__init__(*groups)
        self.image = pygame.image.load('./graphics/bonus/1.png')
        self.rect = self.image.get_rect(center = pos)
        self.centery = self.rect.centery
        
    def move(self,dt):
        if self.rect.bottom < HEIGHT:
            self.centery += Directions.DOWN.value.y * dt * SPEED_OF_BONUS
        self.rect.centery = self.centery
    
    def update(self, dt):
        self.move(dt)
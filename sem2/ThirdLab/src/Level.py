from settings import *
from Player import Player
from BulletManager import BulletManager


class Level:
    
    def __init__(self,display:pygame.surface.Surface): 
        self.setup(display)
        
    def setup(self,display:pygame.surface.Surface):
        self.screen = display
        
        self.bm = BulletManager()
        
        self.sprites = pygame.sprite.GroupSingle()
        self.sprites.add(Player(self.sprites,self.bm))
        
    def update(self,dt:float):
        self.screen.fill('red')
        
        self.bm.update(dt)
        self.sprites.update(dt)
        
        self.sprites.draw(self.screen)
        self.bm.draw(self.screen)
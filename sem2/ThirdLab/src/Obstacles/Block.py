from .Obstacle_settings import *

class Block(pygame.sprite.Sprite):
    
    def __init__(self, *groups,pos):
        super().__init__(*groups)
        self.image = pygame.surface.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.image.fill('green')
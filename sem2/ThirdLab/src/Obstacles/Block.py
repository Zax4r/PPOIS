import pygame

class Block(pygame.sprite.Sprite):
    
    def __init__(self, *groups,pos,data):
        super().__init__(*groups)
        self.image = pygame.surface.Surface((data['obstacles']['BLOCK_SIZE'],data['obstacles']['BLOCK_SIZE']))
        self.rect = self.image.get_rect(topleft = pos)
        self.image.fill('green')
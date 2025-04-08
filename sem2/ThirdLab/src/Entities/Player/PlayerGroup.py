import pygame

class PlayerGroup(pygame.sprite.GroupSingle):
        
    def get_hp(self):
        return self.sprites()[0].hp
    
    def get_status(self):
        return self.sprites()[0].get_status()
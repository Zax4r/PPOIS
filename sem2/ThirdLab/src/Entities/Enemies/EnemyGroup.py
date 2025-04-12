import pygame
from .EnemyGroupI import EnemyGroupI
import random

class EnemyGroup(EnemyGroupI):
    
    def __init__(self, *sprites,bm,data):
        self.data = data
        super().__init__(*sprites)
        self.bm = bm
        self.direction_of_moving = 1
        self.can_shoot = {}
        self.delay = self.data['enemy']['DELAY_BETWEEN_SHOTS_ENEMIES']
        
    def load(self, enemies_layers):
        for layer in enemies_layers:
            self.add(layer)
            
    def update(self,dt):
        self.delay += dt
        self.can_shoot = {}
        self.minleft,self.maxright = self.data['WIDTH'],0
        for sprite in self.sprites():
            sprite.update(dt,self.direction_of_moving)
            rect = sprite.getrect
            self.minleft = min(self.minleft,rect.left)
            self.maxright = max(self.maxright,rect.right)
            self.can_shoot[rect.centerx] = sprite
        
        if self.delay >= self.data['enemy']['DELAY_BETWEEN_SHOTS_ENEMIES'] and len(self.can_shoot.items()):
            key = random.choice(list(self.can_shoot.keys()))   
            self.can_shoot[key].shoot()
            self.delay = 0

            

        if self.minleft <= self.data['enemy']['MARGIN_OF_ENEMIES_X']:    
            self.direction_of_moving = 1
            self.step()
        elif self.maxright >= self.data['WIDTH']-self.data['enemy']['MARGIN_OF_ENEMIES_X']:    
            self.direction_of_moving = -1
            self.step()
    
    def step(self):
        for sprite in self.sprites():
            sprite.rect.centery += self.data['enemy']['STEP_ENEMIES']
            
    def find_lowest(self):
        if self.sprites():
            lowest = 0
            self.lowest_sprite = self.sprites()[0]
            for value in self.can_shoot.values():
                if value.getrect.centery > lowest:
                    lowest = value.getrect.centery
                    self.lowest_sprite = value
            return lowest
        return 0
    
    def remove_lowest(self):
        self.remove(self.lowest_sprite)
    
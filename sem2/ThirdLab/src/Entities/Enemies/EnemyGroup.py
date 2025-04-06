from .settings import *
from .EnemyGroupI import EnemyGroupI
import random

class EnemyGroup(EnemyGroupI):
    
    def __init__(self, *sprites,bm):
        super().__init__(*sprites)
        self.bm = bm
        self.direction_of_moving = 1
        self.can_shoot = {}
        self.delay = DELAY_BETWEEN_SHOTS_ENEMIES
        
    def load(self, enemies_layers):
        for layer in enemies_layers:
            self.add(layer)
            
    def update(self,dt):
        self.delay += dt
        self.can_shoot = {}
        self.minleft,self.maxright = WIDTH,0
        for sprite in self.sprites():
            sprite.update(dt,self.direction_of_moving)
            rect = sprite.getrect
            self.minleft = min(self.minleft,rect.left)
            self.maxright = max(self.maxright,rect.right)
            self.can_shoot[rect.centerx] = sprite
        
        if self.delay >= DELAY_BETWEEN_SHOTS_ENEMIES and len(self.can_shoot.items()):
            key = random.choice(list(self.can_shoot.keys()))   
            self.can_shoot[key].shoot()
            self.delay = 0

            
            
        if self.minleft <= MARGIN_OF_ENEMIES_X:    
            self.direction_of_moving = 1
        elif self.maxright >= WIDTH-MARGIN_OF_ENEMIES_X:    
            self.direction_of_moving = -1
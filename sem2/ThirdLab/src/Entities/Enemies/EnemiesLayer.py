from .settings import *

class EnemiesLayer(pygame.sprite.Group):
    
    def __init__(self, enemies,bm,starty):
        super().__init__()
        self.length = WIDTH - 2*MARGIN_OF_ENEMIES_X 
        self.startx = MARGIN_OF_ENEMIES_X
        self.starty = starty
        for sprite in enemies:
            self.add(sprite(bm=bm,pos=(self.startx,self.starty)))
            self.startx += MARGIN_BETWEEN_ENEMIES_X + WIDTH_OF_ENEMY
    
    def update(self,dt,direction_of_moving):
        for sprite in self.sprites():
            sprite.update(dt,direction_of_moving)

    
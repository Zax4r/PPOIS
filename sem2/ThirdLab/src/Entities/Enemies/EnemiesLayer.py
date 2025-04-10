import pygame

class EnemiesLayer(pygame.sprite.Group):
    
    def __init__(self, enemies,bm,starty,data):
        self.data = data
        super().__init__()
        self.length = self.data['WIDTH'] - 2*self.data['enemy']['MARGIN_OF_ENEMIES_X'] 
        self.startx = self.data['enemy']['MARGIN_OF_ENEMIES_X'] 
        self.starty = starty
        for sprite in enemies:
            self.add(sprite(bm=bm,pos=(self.startx,self.starty),data=self.data))
            self.startx += self.data['enemy']['MARGIN_BETWEEN_ENEMIES_X'] + self.data['enemy']['WIDTH_OF_ENEMY']
    
    def update(self,dt,direction_of_moving):
        for sprite in self.sprites():
            sprite.update(dt,direction_of_moving)

    
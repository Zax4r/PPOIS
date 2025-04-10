from .Obstacle import Obstacle
import pygame

class ObstacleGroup(pygame.sprite.Group):
    
    def __init__(self, *sprites,data):
        super().__init__(*sprites)
        startx = data['obstacles']['MARGIN_OBSTACLE']
        for i in range(4):
            self.add(Obstacle(self,pos=(startx,data['obstacles']['START_HEIGHT_OBSTACLES']),data=data))
            startx +=data['obstacles']['GAP_BETWEEN_OBSTACLES']
    
from .Obstacle import Obstacle
from .Obstacle_settings import *

class ObstacleGroup(pygame.sprite.Group):
    
    def __init__(self, *sprites):
        super().__init__(*sprites)
        startx = MARGIN_OBSTACLE
        for i in range(4):
            self.add(Obstacle(self,pos=(startx,START_HEIGHT_OBSTACLES)))
            startx +=GAP_BETWEEN_OBSTACLES
    
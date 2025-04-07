from ..Entity import *
import random
from .settings import *

class EnemyI(Entity):
    
    def __init__(self, *groups,bm,hp,img,score):
        img = pygame.transform.scale(img,(WIDTH_OF_ENEMY,HEIGHT_OF_ENEMY))
        super().__init__(*groups,bm=bm,hp=hp,img=img)
        self.score = score
        self.aim = Directions.DOWN

    def update_image(self, img):
        img = pygame.transform.scale(img,(WIDTH_OF_ENEMY,HEIGHT_OF_ENEMY))
        self.image = img
        
    def kill(self):
        super().kill()
        return self.score
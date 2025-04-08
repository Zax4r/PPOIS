from .EnemyGroupI import EnemyGroupI
from .EnemiesLayer import EnemiesLayer
from .settings import *
from .levels import *

class EnemyLoader:
    
    def __init__(self,bm):
        self.starty = MARGIN_OF_ENEMIES_Y
        self.bm= bm
    
    def load(self,EG:EnemyGroupI,level):
        self.starty = MARGIN_OF_ENEMIES_Y
        res = []
        for layer,enemies in levels[level].items():
            enemies_classes = []
            if layer.startswith("layer"):
                for enemy_name in enemies:
                    enemies_classes.append(enemies_dict[enemy_name])
                res.append(EnemiesLayer(enemies_classes,bm=self.bm,starty=self.starty))
                self.starty += MARGIN_BETWEEN_ENEMIES_Y + HEIGHT_OF_ENEMY
        EG.load(res)
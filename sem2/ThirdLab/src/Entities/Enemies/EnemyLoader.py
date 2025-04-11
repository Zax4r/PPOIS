from .EnemyGroupI import EnemyGroupI
from .EnemiesLayer import EnemiesLayer
from .enemies_dict import *

class EnemyLoader:
    
    def __init__(self,bm,data):
        self.data = data
        self.starty = self.data['enemy']['MARGIN_OF_ENEMIES_Y']
        self.bm= bm
    
    def load(self,EG:EnemyGroupI,level):
        level = str(level)
        self.starty = self.data['enemy']['MARGIN_OF_ENEMIES_Y']
        res = []
        for layer,enemies in self.data['levels'][level].items():
            enemies_classes = []
            if layer.startswith("layer"):
                for enemy_name in enemies:
                    enemies_classes.append(enemies_dict[enemy_name])
                res.append(EnemiesLayer(enemies_classes,bm=self.bm,starty=self.starty,data = self.data))
                self.starty += self.data['enemy']['MARGIN_BETWEEN_ENEMIES_Y'] + self.data['enemy']['HEIGHT_OF_ENEMY']
        EG.load(res)
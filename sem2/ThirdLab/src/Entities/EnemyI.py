from .Entity import Entity

from .settings import *

class EnemyI(Entity):
    
    def __init__(self, *groups,bm,hp):
        super().__init__(*groups,bm=bm,hp=hp)
        self.aim = Directions.DOWN

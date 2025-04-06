from Entity import Entity
from InputI import InputI

from settings import *

class PlayerI(Entity,InputI):
    
    def __init__(self, *groups,bm,hp):
        super().__init__(*groups,bm=bm,hp=hp)
        self.aim = Directions.UP
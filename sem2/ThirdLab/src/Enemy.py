from Entity import Entity
import abc
from settings import *
from BulletManager import BulletManager


class Enemy(Entity):
    
    def __init__(self, *groups,bm:BulletManager,pos,direction):
        super().__init__(*groups,bm=bm)
        self.shooting_direction = Directions.DOWN

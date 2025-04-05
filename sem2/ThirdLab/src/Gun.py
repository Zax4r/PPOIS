from settings import *
from typing import List
from BulletManager import BulletManager
import abc

class Gun(abc.ABC):
    
    def __init__(self,bm:BulletManager,direction:Directions):
        super().__init__()
        self.bm = bm
        self.direction = direction.value
        
    @abc.abstractmethod
    def shoot(self,pos:pygame.Vector2):
        pass

    
    
    
from settings import *
from ..BulletManager.BulletManagerI import BulletManagerI
import abc

class Gun(abc.ABC):
    
    def __init__(self,bm:BulletManagerI,direction:Directions):
        super().__init__()
        self.bm = bm
        self.direction = direction.value
        
    @abc.abstractmethod
    def shoot(self,pos:pygame.Vector2):
        pass

    
    
    
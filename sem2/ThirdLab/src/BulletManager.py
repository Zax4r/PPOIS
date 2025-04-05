from settings import *
from Bullet import Bullet
#Можно было унаследовать от sprite.Group
class BulletManager:
    
    def __init__(self):
        self.bullets = pygame.sprite.Group()
    
    def add_bullet(self,bullet:Bullet):
        self.bullets.add(bullet)
        
    def update(self,dt):
        self.bullets.update(dt)
        
    def draw(self,screen:pygame.surface.Surface):
        self.bullets.draw(screen)
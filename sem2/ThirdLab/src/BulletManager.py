from settings import *
from BulletManagerI import BulletManagerI

class BulletManager(BulletManagerI):
    
    def __init__(self, *sprites):
        super().__init__(*sprites)
    
    def add_bullet(self,bullet):
        self.add(bullet)
        
    def update(self,dt):
        for sprite in self.sprites():
            sprite.update(dt)
        self.delete_exited()
        
    def delete_exited(self):
        for bullet in self.sprites():
            if bullet.getrecty < 0 or bullet.getrecty > HEIGHT:
                self.remove(bullet)
    
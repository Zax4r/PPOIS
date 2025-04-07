from ..EnemyI import *


class FirstEnemy(EnemyI):
    
    def __init__(self, *groups, bm,pos):
        image = pygame.surface.Surface((200,200))
        super().__init__(*groups, bm=bm,hp = HP_OF_FIRST_ENEMY,img=image,score=SCORES_FIRST_ENEMY)     
    
        self.rect.topleft = pos
        self.centerx = self.rect.centerx
        self.image.fill('yellow')
        self.gun = FirstGun(self.bm,self.aim)            
            
    def move(self,dt,direction_of_moving):
        self.centerx += direction_of_moving * SPEED_OF_ENEMY * dt
        self.rect.centerx = self.centerx
        
    def shoot(self):
        self.gun.shoot(self.rect.center)
    
    def update(self,dt,direction_of_moving):
        self.move(dt,direction_of_moving)
        
    def kill(self):
        super().kill()
        
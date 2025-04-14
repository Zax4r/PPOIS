from ..EnemyI import *

class SeventhEnemy(EnemyI):
    
    def __init__(self, *groups, bm,pos,data):
        self.import_assets('./graphics/enemies/seventh')
        self.animation_index = 0
        super().__init__(*groups, bm=bm,img=self.moving_animations[self.animation_index],data=data,score=data['enemy']['SCORES_SEVENTH_ENEMY'])     
    
        self.rect.topleft = pos
        self.centerx = self.rect.centerx
        self.gun = SecondGun(self.bm,self.aim,self.data)            
                    
    def move(self,dt,direction_of_moving):
        self.centerx += direction_of_moving * self.data['enemy']['SPEED_OF_ENEMY'] * dt
        self.rect.centerx = self.centerx
        
    def shoot(self):
        self.gun.shoot(self.rect.center)
    
    def update(self,dt,direction_of_moving):
        self.move(dt,direction_of_moving)
        self.animate()

        
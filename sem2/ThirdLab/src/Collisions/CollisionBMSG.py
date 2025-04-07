from .Collision import Collision
import random

class CollisionBMSG(Collision):
        
    def check_collision(self,first,second):
        for bullet in first.sprites():
            rect_bullet = bullet.rect
            for sprite in second.sprites():
                if rect_bullet.colliderect(sprite.rect):
                    return bullet,sprite
        return None,None
                
    def collision(self, first, second):
        bullet,sprite = self.check_collision(first,second)
        if bullet and sprite:
            return self.work_with_collision(bullet,sprite,first,second)
        return None,None
    
    def work_with_collision(self, sprite1, sprite2, first, second):
        first.remove(sprite1)
        if not sprite2.update_hp(sprite1.dmg):
            second.remove(sprite2)
            pos,scores = sprite2.rect.center,sprite2.score
            return pos,scores
        return None,None
            

            
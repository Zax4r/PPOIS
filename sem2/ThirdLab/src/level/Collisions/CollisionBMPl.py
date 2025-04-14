from .Collision import Collision
import pygame

class CollisionBmPl(Collision):
        
    def check_collision(self,first,second):
        for bullet in first.sprites():
            rect_bullet = bullet.rect
            for sprite in second.sprites():
                if rect_bullet.colliderect(sprite.rect):
                    yield bullet,sprite
                
    def collision(self, first, second):
        for bullet,sprite in self.check_collision(first,second):
            self.work_with_collision(bullet,sprite,first,second)
    
    def work_with_collision(self, sprite1, sprite2, first, second):
        first.remove(sprite1)
        second.update_hp(1)
        

            
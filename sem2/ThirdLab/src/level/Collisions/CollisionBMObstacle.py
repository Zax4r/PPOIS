from .Collision import Collision

class CollisionBMObstacle(Collision):
    
    def check_collision(self,first,second):
        for bullet in first.sprites():
            rect_bullet = bullet.rect
            for another_bullet in second.sprites():
                if rect_bullet.colliderect(another_bullet.rect):
                    yield bullet,another_bullet
                    break
                
    def collision(self, first, second):
        for bullet,sprite in self.check_collision(first,second):
            self.work_with_collision(bullet,sprite,first,second)
    
    def work_with_collision(self, sprite1, sprite2, first, second):
        first.remove(sprite1)
        second.remove(sprite2)
            

from .CollisionI import Collision

class CollisionBMSG(Collision):

    def __init__(self):
        super().__init__()
        self.count_of_Green = 255
        
    
    def check_collision(self,first,second):
        for bullet in first.sprites():
            rect_bullet = bullet.rect
            for sprite in second.sprites():
                if rect_bullet.colliderect(sprite.rect):
                    yield bullet,sprite
                    break
                
    def collision(self, first, second):
        for bullet,sprite in self.check_collision(first,second):
            self.work_with_collision(bullet,sprite,first,second)
    
    def work_with_collision(self, sprite1, sprite2, first, second):
        first.remove(sprite1)
        if not sprite2.update_hp(sprite1.dmg):
            second.remove(sprite2)
            sprite2.kill()

            
from .Collision import Collision

class CollisionPBonus(Collision):
    
    def check_collision(self,first,second):
        for bonus in first.sprites():
            rect_bonus = bonus.rect
            for player in second.sprites():
                if rect_bonus.colliderect(player.rect):
                    yield bonus,player
                    break
                
    def collision(self, first, second):
        for bonus,sprite in self.check_collision(first,second):
            self.work_with_collision(bonus,sprite,first,second)
    
    def work_with_collision(self, sprite1, sprite2, first, second):
        first.remove(sprite1)
        sprite2.upgrade_gun()
from .Collision import Collision

class CollisionPlEg(Collision):
    
    def check_collision(self,first,second):
        for player in first.sprites():
            rect_player = player.rect
            for enemy in second.sprites():
                if rect_player.colliderect(enemy.rect):
                    yield player,enemy
                    break
                
    def collision(self, first, second):
        for player,enemy in self.check_collision(first,second):
            self.work_with_collision(player,enemy,first,second)
    
    def work_with_collision(self, sprite1, sprite2, first, second):
        second.remove(sprite2)
        sprite1.update_hp(sprite2.hp)
            
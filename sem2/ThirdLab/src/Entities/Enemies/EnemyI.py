from ..Entity import *
from os import walk
from Directions import Directions


class EnemyI(Entity):
    
    def __init__(self, *groups,bm,img,score,data):
        self.data = data
        img = pygame.transform.scale(img,(data['enemy']['WIDTH_OF_ENEMY'],data['enemy']['HEIGHT_OF_ENEMY']))
        super().__init__(*groups,bm=bm,hp=1,img=img)
        self.score = score
        self.aim = Directions.DOWN

    def update_image(self, img):
        img = pygame.transform.scale(img,(self.data['enemy']['WIDTH_OF_ENEMY'],self.data['enemy']['HEIGHT_OF_ENEMY']))
        self.image = img
    
    def import_assets(self,full_path):
        self.moving_animations = []
        for _,_,img_names in walk(full_path):
            for img_name in img_names:
                self.moving_animations.append(pygame.image.load(full_path+f'/{img_name}'))
    
    def animate(self):
        self.animation_index+=0.03
        if self.animation_index >= len(self.moving_animations):
            self.animation_index = 0
        self.update_image(self.moving_animations[int(self.animation_index)])
    
    def kill(self):
        super().kill()
        return self.score
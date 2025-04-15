from ..Entity import *
from os import walk
from Directions import Directions


class EnemyI(Entity):
    
    def __init__(self, *groups,bm,img,score,data):
        self.data = data
        img = pygame.transform.scale(img,(data['enemy']['WIDTH_OF_ENEMY'],data['enemy']['HEIGHT_OF_ENEMY']))
        super().__init__(*groups,bm=bm,hp=1,img=img)
        self.score = score
        self.time_death = -1
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
        if self.time_death >= 0:
            self.time_death += 0.03
            if self.time_death >= 1:
                self.kill()
                del self
    
    def import_death_animations(self):
        death_animations = []
        path = "./graphics/death"
        for _,_,img_names in walk(path):
            for img_name in img_names:
                img = pygame.image.load(path+f'/{img_name}')
                death_animations.append(img)
        return death_animations

    
    def get_score(self):
        if self.time_death < 0:
            self.moving_animations = self.import_death_animations()
            self.time_death = 0
            self.animation_index = 0.5
            return self.score
        return 0
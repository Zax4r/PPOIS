from .PlayerI import PlayerI
import pygame
from os import walk

class Player(PlayerI):
    
    def __init__(self, *group,bm,data):
        self.data = data
        self.import_assets()
        self.status = "idle"
        self.level_of_gun = 1
        super().__init__(*group,bm=bm,hp=self.data['player']['HP_PLAYER'],img=self.animations[self.status][self.level_of_gun-1])
        self.rect = self.image.get_rect()
        self.setup()
        
    def import_assets(self):
        self.animations = {"idle":[],"moving":[]} 
        for name in self.animations.keys():
            full_path = './graphics/player/'+name
            
            for _,_,img_names in walk(full_path):
                for img_name in img_names:
                    self.animations[name].insert(0,pygame.image.load(full_path+f'/{img_name}'))
    
    def setup(self):
        self.direction_of_moving = 0
        self.rect.centerx = self.data['WIDTH']/2 - self.data['player']['WIDTH_OF_PLAYER']/2
        self.rect.centery = self.data['HEIGHT'] - self.data['player']['HEIGHT_OF_PLAYER']/2
        self.centerx = self.rect.centerx
        self.shooting = False
        self.gun = self.available_guns[self.level_of_gun](self.bm,self.aim)
        self.delay =self.data['player']['DELAY_BETWEEN_SHOTS']

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction_of_moving = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.shooting = keys[pygame.K_SPACE]
        if self.direction_of_moving != 0:
            self.status = 'moving'
        else:
            self.status = 'idle'
            
    def move(self,dt):
        if self.rect.left>0 and self.direction_of_moving == -1:
            self.centerx += self.direction_of_moving * self.data['player']['SPEED_OF_PLAYER'] * dt
            self.rect.centerx = self.centerx
        elif self.rect.right<self.data['WIDTH'] and self.direction_of_moving == 1:
            self.centerx += self.direction_of_moving * self.data['player']['SPEED_OF_PLAYER'] * dt
            self.rect.centerx = self.centerx
        
    def shoot(self):
        if self.shooting and self.delay >= self.data['player']['DELAY_BETWEEN_SHOTS']:
            self.gun.shoot(self.rect.center)
            self.delay = 0
    
    def update(self,dt):
        self.delay +=dt
        self.input()
        self.move(dt)
        self.shoot()
        self.update_image()
        
    def update_image(self):
        self.image = self.animations[self.status][self.level_of_gun-1]
        self.image = pygame.transform.scale(self.image,(self.rect.size))
        
    def upgrade_gun(self):
        if self.level_of_gun > 2:
            return
        self.level_of_gun += 1
        self.gun = self.available_guns[self.level_of_gun](self.bm,self.aim)
        

        
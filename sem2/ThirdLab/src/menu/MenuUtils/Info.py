import pygame
from os import walk
from .InfoPlate import InfoPlate


class Info:
    
    def __init__(self,screen,data):
        self.data = data
        self.screen = screen
        self.font = pygame.font.Font(None,35)
        self.get_enemy_images()
        self.create_info_plates()
        self.create_info_player()
        
    def get_enemy_images(self):
        self.images = {}
        path = './graphics/enemies/'
        for full_path,_,file_names in walk(path):
            
            if len(file_names):
                key = full_path.split('/')[-1]
                self.images[key]=pygame.image.load(f"{full_path}/{file_names[0]}")
        
    def create_info_plates(self):
        self.info_plates = []
        startx,starty = self.data['info']['MARGIN_OF_PLATE_X'],self.data['info']['MARGIN_OF_PLATE_Y']
        i = 0
        for key,img in self.images.items():
            self.info_plates.append(InfoPlate(img,key,self.data,(startx,starty)))
            starty += self.data['info']['GAP_BETWEEN_PLATES']
            i+=1
            if i == len(self.images.items())//2:
                startx += self.data['info']['GAP_BETWEEN_COLUMNS']
                starty = self.data['info']['MARGIN_OF_PLATE_Y']
                
    def create_info_player(self):
        self.plyer_info_surf = self.font.render("Управление:A = влево, D = вправо, SPACE = стрелять",True,"white")
        self.player_info_surf_rect = self.plyer_info_surf.get_rect(topleft = (0,0))
        self.goal_of_game_surf = self.font.render("Цель: заработать как можно больше очков/ продержаться все 20 волн",True,"white")
        self.goal_of_game_surf_rect = self.goal_of_game_surf.get_rect(topleft = (0,50))
        self.bonus_surf = self.font.render("Во время игры с врагов будут выпадать бонусы(оружие/аптечки)",True,"white")
        self.bonus_surf_rect = self.bonus_surf.get_rect(topleft = (0,90))
        self.leave_surf = self.font.render("Чтобы выйти нажмите ESC",True,"white")
        self.leave_surf_rect = self.leave_surf.get_rect(bottomleft = (0,self.data['HEIGHT']))
    
    def update(self):
        self.screen.fill('black')
        for plate in self.info_plates:
            plate.draw(self.screen)
        self.screen.blit(self.plyer_info_surf,self.player_info_surf_rect)
        self.screen.blit(self.goal_of_game_surf,self.goal_of_game_surf_rect)
        self.screen.blit(self.bonus_surf,self.bonus_surf_rect)
        self.screen.blit(self.leave_surf,self.leave_surf_rect)
    

    

    
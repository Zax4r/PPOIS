import pygame

class InfoPlate:
    
    def __init__(self,img,name,data,pos):
        self.img = pygame.transform.scale(img,(data['enemy']["WIDTH_OF_ENEMY"],data['enemy']['HEIGHT_OF_ENEMY']))
        self.score = -1
        for key in data['enemy'].keys():
            if name in key.lower():
                self.score = data['enemy'][key]
        self.title = name
        self.pos = pos
        self.text_font = pygame.font.Font(None,35)
        self.create_surfaces()
        
    def create_surfaces(self):
        self.img_rect = self.img.get_rect(topright = self.pos)
        self.title_score_surf = self.text_font.render(f"{self.title}: scores{self.score}",True,'white')
        self.title_score_rect = self.title_score_surf.get_rect(topleft = self.pos)    
    
    def draw(self,screen):
        screen.blit(self.img,self.img_rect)
        screen.blit(self.title_score_surf,self.title_score_rect)
        
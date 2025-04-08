import pygame

class MenuButton():
    
    def __init__(self,text,width,height,pos):
        
        self.pressed = False
        
        self.top_rect = pygame.rect.Rect(pos,(width,height))
        self.top_rect.center = pos
        self.bgcolor = 'blue'
        gui_font = pygame.font.Font(None,30)
        self.text_surf = gui_font.render(text,False,'white')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        
    def draw(self,screen):
        pygame.draw.rect(screen,self.bgcolor,self.top_rect)
        screen.blit(self.text_surf,self.text_rect)
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.bgcolor = 'skyblue'
            if pygame.mouse.get_pressed()[0] and not self.pressed:
                self.pressed = True
                return True
        else:
            self.bgcolor = 'blue'
        return False
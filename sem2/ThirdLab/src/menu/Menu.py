from .MenuUtils.MenuButton  import MenuButton
from .MenuUtils.PlayerDatabase import PlayerDatabase
from .MenuUtils.TableRecords import TableRecords
from .MenuUtils.Info import Info
import pygame
import sys

class Menu:
    
    def __init__(self,screen,data):
        self.data = data
        self.db = PlayerDatabase()
        full_path = './graphics/menu/BG.png'
        self.bg = pygame.image.load(full_path)
        self.bg = pygame.transform.scale(self.bg,(self.data['WIDTH'],self.data['HEIGHT']))
        self.screen = screen
        self.states = ["Играть","Справка","Таблица записей","Выход"]
        self.state = 'Меню'
        self.buttons = []
        self.info = Info(self.screen,self.data)
        self.table_up_to_date = False
        self.table = TableRecords(self.screen,self.data)
        for i,state in enumerate(self.states):
            self.buttons.append(MenuButton(state,200,80,(self.data['WIDTH']/4,(i+1)*100)))
            
    def add_record(self,new_name,new_score):
        if new_name:
            self.db.add_player(new_name,new_score)
            self.table_up_to_date = False
        
    def input(self):
        self.screen.blit(self.bg,(0,0))
        for i,button in enumerate(self.buttons):
            button.draw(self.screen)
            self.pressed = button.check_click()
            if self.pressed:
                self.state = self.states[i]

    def get_top(self):
        try:
            res = self.db.get_all_players()[-1]
            return res[1]
        except IndexError:
            return 0
    
    def update(self):       
        if self.state == 'Меню':
            self.input()
        elif self.state == 'Играть':
            return True
        elif self.state == 'Выход':
            pygame.quit()
            sys.exit()
        elif self.state == 'Таблица записей':
            if not self.table_up_to_date:
                self.table.update_records(self.db.get_all_players()[::-1][:5])
                self.table_up_to_date = True
            self.table.update()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.state = "Меню"
        elif self.state == "Справка":
            self.info.update()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.state = "Меню"
            
            
        else:
            return False


       
                
        
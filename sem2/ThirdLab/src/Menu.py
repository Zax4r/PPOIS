from MenuUtils.MenuButton  import MenuButton
from MenuUtils.PlayerDatabase import PlayerDatabase
from MenuUtils.TableRecords import TableRecords
from settings import *
import sys

class Menu:
    
    def __init__(self,screen):
        self.db = PlayerDatabase()
        self.screen = screen
        self.states = ["Играть","Справка","Таблица записей","Выход"]
        self.state = 'Меню'
        self.buttons = []
        self.table = TableRecords(self.screen,self.db.get_all_players()[::-1][:10])
        for i,state in enumerate(self.states):
            self.buttons.append(MenuButton(state,200,80,(WIDTH/4,(i+1)*100)))
            
    def add_record(self,new_name,new_score):
        if new_name:
            self.db.add_player(new_name,new_score)
        
    def input(self):
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
        self.screen.fill('grey')
        
        if self.state == 'Меню':
            self.input()
        elif self.state == 'Играть':
            return True
        elif self.state == 'Выход':
            pygame.quit()
            sys.exit()
        elif self.state == 'Таблица записей':
            self.table.update()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.state = "Меню"
            
        else:return False


       
                
        
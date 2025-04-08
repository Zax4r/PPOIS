from MenuButton  import MenuButton
from settings import *

class Menu:
    
    def __init__(self,screen):
        self.screen = screen
        self.states = ["Играть","Справка","Таблица записей","Выход"]
        self.state = 'Меню'
        self.pressed = False
        self.buttons = []
        for i,state in enumerate(self.states):
            self.buttons.append(MenuButton(state,200,80,(WIDTH/4,(i+1)*100)))
        
    def input(self):
        for i,button in enumerate(self.buttons):
            button.draw(self.screen)
            self.pressed = button.check_click()
            if self.pressed:
                self.state = self.states[i]
                self.pressed = False
                print(self.state)

    def update(self):
        self.screen.fill('grey')
        self.input()
        if self.state == 'Играть':
            return True
        else:return False


       
                
        
import sys
from Level import Level
from Menu import Menu
from settings import *

class States(Enum):
    GAME = 1
    MENU = 2


class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("ЗАЛУПА ЕЖА")
        self.clock = pygame.time.Clock()
        self.state = States.MENU
        self.running = True
        self.time = pygame.time.Clock()
        self.level = Level(self.screen,-1)
        self.menu = Menu(self.screen)
        self.new_name,self.record = None,-1
        
    def run(self):
        while self.running:
            
            dt = self.clock.tick(60)/1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
            
            if self.state is States.GAME:  
                self.new_name,self.record = self.level.update(dt)
                if self.new_name is not None:
                    self.state = States.MENU
                    self.menu = Menu(self.screen)
            elif self.state is States.MENU:
                self.start_game = self.menu.update()
                if self.start_game:
                    self.state = States.GAME
                    self.level = Level(self.screen,-10)
                    self.start_game = False
            pygame.display.update()
    
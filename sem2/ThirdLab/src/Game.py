import sys
import json
from level.Level import Level
from menu.Menu import Menu
import pygame
from enum import Enum

class States(Enum):
    GAME = 1
    MENU = 2


class Game:
    
    def __init__(self):
        pygame.init()
        
        with open('settings.json','r') as file:
            self.data = json.load(file)
        self.music = pygame.mixer.Sound('./audio/music.wav')
        self.music.set_volume(0.1)
        self.music.play(loops=-1)
        self.screen = pygame.display.set_mode((self.data['WIDTH'],self.data['HEIGHT']))
        pygame.display.set_caption("Галактические захватчики")
        self.clock = pygame.time.Clock()
        self.state = States.MENU
        self.running = True
        self.time = pygame.time.Clock()
        self.menu = Menu(self.screen,self.data)
        
    def run(self):
        while self.running:
            
            dt = self.clock.tick(60)/1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    self.running = False
                    
            
            if self.state is States.GAME:  
                self.new_name,self.new_score = self.level.update(dt)
                if self.new_name is not None:
                    self.state = States.MENU
                    self.menu = Menu(self.screen,self.data)
                    self.menu.add_record(self.new_name,self.new_score)
        
            elif self.state is States.MENU:
                self.start_game = self.menu.update()
                if self.start_game:
                    self.top_score = self.menu.get_top()
                    self.state = States.GAME
                    self.level = Level(self.screen,self.top_score,self.data)
                    self.start_game = False
                    
            pygame.display.update()
    
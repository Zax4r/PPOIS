import sys
from Level import Level
from settings import *

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("ЗАЛУПА ЕЖА")
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.time = pygame.time.Clock()
        self.level = Level(self.screen)
        
    def run(self):
        while self.running:
            
            dt = self.clock.tick()/1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                
            self.level.update(dt)
            pygame.display.update()
    
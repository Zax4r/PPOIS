from settings import *
from Player import Player
from BulletManager import BulletManager
from FirstEnemy import FirstEnemy

class Level:
    
    def __init__(self,display:pygame.surface.Surface): 
        self.setup(display)
        
    def setup(self,display:pygame.surface.Surface):
        self.screen = display
        
        self.bm_player = BulletManager()
        self.bm_enemy = BulletManager()
        
        self.enemy_sprite = pygame.sprite.GroupSingle()
        self.enemy_sprite.add(FirstEnemy(self.enemy_sprite,bm=self.bm_enemy,pos=(WIDTH/2,HEIGHT/2),direction=-1))
        
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player_sprite.add(Player(self.player_sprite,self.bm_player))
        
    def update(self,dt:float):
        self.screen.fill('red')
        
        self.bm_player.update(dt)
        self.player_sprite.update(dt)
        self.bm_enemy.update(dt)
        self.enemy_sprite.update(dt)
        
        self.enemy_sprite.draw(self.screen)
        self.player_sprite.draw(self.screen)
        self.bm_player.draw(self.screen)
        self.bm_enemy.draw(self.screen)
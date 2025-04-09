from settings import *

from Entities.Player.Player import Player
from Entities.Player.PlayerGroup import PlayerGroup
from Entities.BulletManager.BulletManager import BulletManager
from Entities.Enemies.EnemyLoader import EnemyLoader
from Entities.Enemies.EnemyGroup import EnemyGroup

from Bonus.Bonus import Bonus

from GameOver.GameOver import GameOver

from Collisions.CollisionBMBM import CollisionBMBM
from Collisions.CollisionBMObstacle import CollisionBMObstacle
from Collisions.CollisionBMEnm import CollisionBmEnm
from Collisions.CollisionBMPl import CollisionBmPl
from Collisions.CollisionPBonus import CollisionPBonus
from Collisions.CollisionPlEg import CollisionPlEg

from Obstacles.ObstacleGroup import ObstacleGroup

class Level:
    
    def __init__(self,display:pygame.surface.Surface,top_score): 
        self.setup(display,top_score)
        
    def setup(self,display:pygame.surface.Surface,top_score):
        self.top_score = top_score
        self.all_scores = 0
        self.temp_scores = 0
        self.level = 1
        self.keep_running = True
        
        self.screen = display
        self.score_font = pygame.font.Font(None,40)
        self.hp_font = pygame.font.Font(None,40)
        
        self.name = None

        self.game_over = GameOver(self)
        
        self._create_collisions()
        self._create_groups()
        
        self.player_sprite.add(Player(self.player_sprite,bm = self.bm_player))
    
    def _load_level(self):
        if not len(self.enemy_sprites.sprites()):
            self.enemy_loader.load(self.enemy_sprites,self.level)
            self.level += 1
            
    def _create_groups(self):
        self.bm_player = BulletManager()
        self.bm_enemy = BulletManager()
        
        self.bonus_group = pygame.sprite.Group()
        
        self.obstacle_group = ObstacleGroup()
        
        self.enemy_sprites = EnemyGroup(bm=self.bm_enemy)
        self.enemy_loader = EnemyLoader(bm=self.bm_enemy)
        
        self.player_sprite = PlayerGroup()
    
    def _create_collisions(self):
        self.collider_bmbm = CollisionBMBM()

        self.collider_bmpl = CollisionBmPl()
        self.collider_bmenm = CollisionBmEnm()
        
        self.collider_bmobs = CollisionBMObstacle()
        self.colliderpbonus = CollisionPBonus()
        self.collider_pleg = CollisionPlEg()   

    def recieve_name(self,name):
        self.name = name

    def _collisions(self):
        self.collider_bmbm.collision(self.bm_enemy,self.bm_player)
        self.collider_bmpl.collision(self.bm_enemy,self.player_sprite)
        
        self.collider_bmobs.collision(self.bm_enemy,self.obstacle_group)
        self.collider_bmobs.collision(self.bm_player,self.obstacle_group)
        
        self.colliderpbonus.collision(self.bonus_group,self.player_sprite)
        
        self.collider_pleg.collision(self.player_sprite,self.enemy_sprites)
        
        pos,scores = self.collider_bmenm.collision(self.bm_player,self.enemy_sprites)
        if scores:
            self.temp_scores += scores
            self.all_scores += scores
        if pos and self.temp_scores>=250:
            self.bonus_group.add(Bonus(self.bonus_group,pos=pos))
            self.temp_scores %= 250
    
    def draw_text(self):
        scores_s = self.score_font.render(f"Scores: {self.all_scores}",True,'yellow')
        self.screen.blit(scores_s,(0,0))
        
        hp_s = self.hp_font.render(f"HP:{self.player_sprite.get_hp()}",True,'brown')
        self.screen.blit(hp_s,(WIDTH-100,HEIGHT-100))    
    
    def update(self,dt:float):
        self.screen.fill('black')
        
        if self.keep_running:
            
            self.bm_player.update(dt)
            self.player_sprite.update(dt)
            self.bm_enemy.update(dt)
            self.enemy_sprites.update(dt)
            self.bonus_group.update(dt)
            
            self._collisions()
            
            self.bm_player.draw(self.screen)
            self.player_sprite.draw(self.screen)
            
            self.enemy_sprites.draw(self.screen)
            self.bm_enemy.draw(self.screen)
            self.bonus_group.draw(self.screen)
            
            self.obstacle_group.draw(self.screen)
            
            self.draw_text()
            
            try:
                self._load_level()
            except KeyError:
                self.keep_running = False

        if not self.keep_running:
            name = self.game_over.show_game_over()
            return name,self.all_scores
            
        self.keep_running = self.player_sprite.get_status()
        return None,None
from settings import *

from Entities.Player.Player import Player
from Entities.BulletManager.BulletManager import BulletManager
from Entities.Enemies.EnemyLoader import EnemyLoader
from Entities.Enemies.EnemyGroup import EnemyGroup

from Entities.Bonus import Bonus

from Collisions.CollisionBMBM import CollisionBMBM
from Collisions.CollisionBMObstacle import CollisionBMObstacle
from Collisions.CollisionBMSG import CollisionBMSG
from Collisions.CollisionPBonus import CollisionPBonus

from Obstacles.ObstacleGroup import ObstacleGroup

class Level:
    
    def __init__(self,display:pygame.surface.Surface): 
        self.setup(display)
        
    def setup(self,display:pygame.surface.Surface):
        self.screen = display
        self.all_scores = 0
        
        self.bm_player = BulletManager()
        self.bm_enemy = BulletManager()
        
        self.bonus_group = pygame.sprite.Group()
        
        self.collider_bmbm = CollisionBMBM()
        self.collider_bmsg = CollisionBMSG()
        self.collider_bmobs = CollisionBMObstacle()
        self.colliderpbonus = CollisionPBonus()
        
        self.obstacle_group = ObstacleGroup()
        
        self.enemy_sprites = EnemyGroup(bm=self.bm_enemy)
        self.enemy_loader = EnemyLoader(bm=self.bm_enemy)
        self.enemy_loader.load(self.enemy_sprites)
        
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player_sprite.add(Player(self.player_sprite,bm = self.bm_player))
        
    def _collisions(self):
        self.collider_bmbm.collision(self.bm_enemy,self.bm_player)
        self.collider_bmsg.collision(self.bm_enemy,self.player_sprite)
        self.collider_bmobs.collision(self.bm_enemy,self.obstacle_group)
        self.collider_bmobs.collision(self.bm_player,self.obstacle_group)
        self.colliderpbonus.collision(self.bonus_group,self.player_sprite)
        
        pos,scores = self.collider_bmsg.collision(self.bm_player,self.enemy_sprites)
        if scores:
            self.all_scores += scores
        if pos and self.all_scores//100:
            self.bonus_group.add(Bonus(self.bonus_group,pos=pos))
            self.all_scores = 0
    
    
    def update(self,dt:float):
        self.screen.fill('black')
        
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
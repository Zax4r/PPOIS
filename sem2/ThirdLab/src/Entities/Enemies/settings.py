import pygame
from enum import Enum

WIDTH = 1000
HEIGHT = 640

class Directions(Enum):
    UP = pygame.Vector2(0,-1)
    DOWN = pygame.Vector2(0,1)
    UPRIGHT45 = pygame.Vector2(1,-1).normalize()
    UPLEFT45 = pygame.Vector2(-1,-1).normalize()
    
SPEED_OF_ENEMY = 150
DELAY_BETWEEN_SHOTS_ENEMIES = 1.5
MARGIN_OF_ENEMIES_X,MARGIN_OF_ENEMIES_Y = 50,50
WIDTH_OF_ENEMY,HEIGHT_OF_ENEMY = 50,50
MARGIN_BETWEEN_ENEMIES_X,MARGIN_BETWEEN_ENEMIES_Y = 20,20
STEP_ENEMIES = 20
#First Enemy Stats
SCORES_FIRST_ENEMY = 40
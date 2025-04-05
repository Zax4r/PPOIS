import pygame
from enum import Enum

WIDTH = 1000
HEIGHT = 640

HEIGHT_OF_PLATE = 20
WIDTH_OF_PLATE = 120
SPEED_OF_PLATE = 1200

DELAY_BETWEEN_SHOTS = 0.5


WIDTH_OF_BULLET = 20
HEIGHT_OF_BULLET = 50
VELOCITY_OF_BULLET = 800

class Directions(Enum):
    UP = pygame.Vector2(0,-1)
    DOWN = pygame.Vector2(0,1)
    UPRIGHT45 = pygame.Vector2(1,-1).normalize()
    UPLEFT45 = pygame.Vector2(-1,-1).normalize()
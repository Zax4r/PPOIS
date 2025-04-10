import pygame
from enum import Enum

WIDTH = 1000
HEIGHT = 640

WIDTH_OF_BULLET = 10
HEIGHT_OF_BULLET = 20
VELOCITY_OF_BULLET = 500

DAMAGE_SIMPLE_BULLET = 10
DAMAGE_BOUNCING_BULLET = 20
DAMAGE_TELEPORTING_BULLET = 25

class Directions(Enum):
    UP = pygame.Vector2(0,-1)
    DOWN = pygame.Vector2(0,1)
    UPRIGHT45 = pygame.Vector2(1,-1).normalize()
    UPLEFT45 = pygame.Vector2(-1,-1).normalize()
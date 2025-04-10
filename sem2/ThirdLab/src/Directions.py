import pygame
from enum import Enum

class Directions(Enum):
    UP = pygame.Vector2(0,-1)
    DOWN = pygame.Vector2(0,1)
    UPRIGHT45 = pygame.Vector2(1,-1).normalize()
    UPLEFT45 = pygame.Vector2(-1,-1).normalize()
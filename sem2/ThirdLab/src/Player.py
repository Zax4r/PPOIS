from PlayerI import PlayerI
from settings import *
from FirstGun import FirstGun
from SecondGun import SecondGun
from ThirdGun import ThirdGun

class Player(PlayerI):
    
    def __init__(self, *group,bm):
        super().__init__(*group,bm=bm,hp=255)
        self.image = pygame.surface.Surface((200,200))
        self.image = pygame.transform.scale(self.image,(WIDTH_OF_PLATE,HEIGHT_OF_PLATE))
        self.rect = self.image.get_rect()
        self.setup()
        
    def setup(self):
        self.direction_of_moving = 0
        self.rect.centerx = WIDTH/2 - WIDTH_OF_PLATE/2
        self.rect.centery = HEIGHT - HEIGHT_OF_PLATE/2
        self.centerx = self.rect.centerx
        self.shooting = False
        self.gun = ThirdGun(self.bm,self.aim)
        self.delay = DELAY_BETWEEN_SHOTS

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction_of_moving = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.shooting = keys[pygame.K_SPACE]
            
    def move(self,dt):
        if self.rect.left>0 and self.direction_of_moving == -1:
            self.centerx += self.direction_of_moving * SPEED_OF_PLATE * dt
            self.rect.centerx = self.centerx
        elif self.rect.right<WIDTH and self.direction_of_moving == 1:
            self.centerx += self.direction_of_moving * SPEED_OF_PLATE * dt
            self.rect.centerx = self.centerx
        
    def shoot(self):
        if self.shooting and self.delay >= DELAY_BETWEEN_SHOTS:
            self.gun.shoot(self.rect.center)
            self.delay = 0
    
    def update(self,dt):
        self.delay +=dt
        self.input()
        self.move(dt)
        self.shoot()
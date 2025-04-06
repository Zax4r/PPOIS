from .Block import Block
from .Obstacle_settings import *

class Obstacle(pygame.sprite.Group):
    
    def __init__(self, *sprites,pos):
        super().__init__(*sprites)
        self.x,self.y = pos
        shape = ["    xxxxx              ",
                 "   xxxxxxx             ",
                 "  xxxxxxxxx           ",
                 " xxxxxxxxxxx          ",
                 "xxxxxxxxxxxxx          "]
        for row_index,row in enumerate(shape):
            for col_index,char in enumerate(row):
                self.x = pos[0] + col_index*BLOCK_SIZE
                self.y = pos[1] + row_index*BLOCK_SIZE
                if char == 'x':
                    self.add(Block(self,pos=(self.x,self.y)))
        
        
    
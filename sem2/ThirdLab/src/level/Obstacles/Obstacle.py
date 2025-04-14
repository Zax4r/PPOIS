from .Block import Block
import pygame

class Obstacle(pygame.sprite.Group):
    
    def __init__(self, *sprites,pos,data):
        super().__init__(*sprites)
        self.x,self.y = pos
        shape = ["    xxxxx              ",
                 "   xxxxxxx             ",
                 "  xxxxxxxxx           ",
                 " xxxxxxxxxxx          ",
                 "xxxxxxxxxxxxx          "]
        for row_index,row in enumerate(shape):
            for col_index,char in enumerate(row):
                self.x = pos[0] + col_index*data['obstacles']['BLOCK_SIZE']
                self.y = pos[1] + row_index*data['obstacles']['BLOCK_SIZE']
                if char == 'x':
                    self.add(Block(self,pos=(self.x,self.y),data=data))
        
        
    
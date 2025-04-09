import pygame
from .table_setting import *

class TableRecords:
    
    def __init__(self,screen,records):
        self.screen = screen
        self.records = records
        self.font = pygame.font.Font(None,40)
    
    def _draw(self):
        leave_surf = self.font.render('Чтобы выйти нажмите ESC',False,'black')
        leave_surf_rect = leave_surf.get_rect(center = (500,500))
        self.screen.blit(leave_surf,leave_surf_rect)
        for i,record in enumerate(self.records):
            record_surf = self.font.render(f'{record[0]} : {record[1]}',False,'gold')
            record_surf_rect = record_surf.get_rect(center = (X_MARGIN,Y_MARGIN + (i*Y_GAP)))
            self.screen.blit(record_surf,record_surf_rect)
    
    def update(self):
        self.screen.fill('blue')
        self._draw()
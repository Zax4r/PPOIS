import pygame

class TableRecords:
    
    def __init__(self,screen,data):
        self.data = data
        self.bg = pygame.image.load('./graphics/menu/records.png')
        self.bg = pygame.transform.scale(self.bg,(self.data['WIDTH'],self.data['HEIGHT']))
        self.screen = screen
        self.records = []
        self.font = pygame.font.Font(None,40)
    
    def _draw(self):
        leave_surf = self.font.render('Чтобы выйти нажмите ESC',False,'grey')
        leave_surf_rect = leave_surf.get_rect(topleft = (0,0))
        self.screen.blit(leave_surf,leave_surf_rect)
        for i,record in enumerate(self.records):
            record_surf = self.font.render(f'{record[0]} : {record[1]}',False,'gold')
            record_surf_rect = record_surf.get_rect(center = (self.data['table']['X_MARGIN'],self.data['table']['Y_MARGIN'] + (i*self.data['table']['Y_GAP'])))
            self.screen.blit(record_surf,record_surf_rect)
    
    def update_records(self,records):
        self.records = records
    
    def update(self):
        self.screen.blit(self.bg,(0,0))
        self._draw()
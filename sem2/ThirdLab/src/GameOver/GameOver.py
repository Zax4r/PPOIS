from .settings import *

class GameOver:
    def __init__(self, level):
        self.level = level
        self.screen = level.screen
        self.font = pygame.font.Font(None, 50)
        self.input_font = pygame.font.Font(None, 40)

    def show_game_over(self):
        self.screen.fill('black')
        game_over_text = self.font.render("GAME OVER", True, 'red')
        score_text = self.font.render(f"Your Score: {self.level.all_scores}", True, 'yellow')
        top_score_text = self.font.render(f"Top Score: {self.level.top_score}", True, 'green')
        leave_text = self.font.render("To leave press Enter",True,'white')

        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        top_score_rect = top_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        leave_text_rect = leave_text.get_rect(center = (WIDTH//2,100))

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(top_score_text, top_score_rect)
        self.screen.blit(leave_text,leave_text_rect)

        if self.level.all_scores > self.level.top_score:
            return self._new_high_score()
        
        else:
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                return ''
        

    def _new_high_score(self):
        
        
        new_high_text = self.font.render("NEW HIGH SCORE!", True, 'gold')
        enter_name_text = self.font.render("Enter Your Name:", True, 'white')

        new_high_rect = new_high_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        enter_name_rect = enter_name_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

        self.screen.blit(new_high_text, new_high_rect)
        self.screen.blit(enter_name_text, enter_name_rect)

        name = ""
        input_active = True
        input_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 200, 200, 50)
        input_color = 'white'

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: 
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE: 
                        name = name[:-1]
                    else:
                        name += event.unicode 

            pygame.draw.rect(self.screen, 'black', input_rect)
            pygame.draw.rect(self.screen, input_color, input_rect, 2)
            name_surface = self.input_font.render(name, True, 'white')
            self.screen.blit(name_surface, (input_rect.x + 10, input_rect.y + 10))

            pygame.display.flip()

        return name
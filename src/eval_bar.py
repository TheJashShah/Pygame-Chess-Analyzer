import pygame

class EvalBar:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = 40

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.white_height = self.height//2

        self.font = pygame.font.SysFont("consolas", 15)

    def draw(self, win, eval_num):
        
        pygame.draw.rect(win, (0, 0, 0), self.rect)
        pygame.draw.rect(win, (255, 255, 255), pygame.Rect(self.x, self.y + self.height - self.white_height, self.width, self.white_height))

        text = self.font.render(format(eval_num), True, (255, 255, 255))
        win.blit(text, text.get_rect(center = (self.x + self.width//2, self.y + 25)))

    def change_bar(self, eval_num):
        
        max_score = 10
        eval_num = max(-max_score, min(eval_num, max_score))

        mid = self.height//2
        scaling_factor = eval_num/max_score

        self.white_height = mid + (scaling_factor * mid)

       
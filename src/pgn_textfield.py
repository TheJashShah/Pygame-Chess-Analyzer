import pygame

class TextField:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width, self.height = 400, 250
        self.string = ""
        self.display_string = "ENTER PGN..."

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.font = pygame.font.SysFont("consolas", 15)

        self.bg = (64, 64, 64)

    def draw(self, win):

        if (len(self.display_string) * 15) >= self.width:
            self.display_string = self.display_string[:(700//15)] + ".."

        pygame.draw.rect(win, (64, 64, 64), self.rect)

        text = self.font.render(self.display_string, True, (255, 255, 255))
        win.blit(text, (self.x + 5, self.y + 2))

        pygame.draw.rect(win, self.bg, pygame.Rect(self.x - 2, self.y - 2, self.width + 4, self.height + 4), 2, 2, 2, 2)


       
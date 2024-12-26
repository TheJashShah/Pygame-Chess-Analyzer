import pygame

class Cell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width, self.height = 80, 80
        self.color = color

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.center = self.rect.center

        self.piece = None
        self.previous = None

        self.mask = pygame.Surface((self.width, self.height))
        self.mask.set_alpha(0)
        self.mask_color = (255, 255, 255)
        

    def draw(self, win):

        pygame.draw.rect(win, self.color, self.rect)

        if self.piece is not None:
            self.piece.x = self.center[0]
            self.piece.y = self.center[1] 
            self.piece.draw(win)

        win.blit(self.mask, (self.x, self.y))

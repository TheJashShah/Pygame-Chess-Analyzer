import pygame

class Button:
    def __init__(self, x, y, text, img):
        self.x = x
        self.y = y
        self.text = text
        self.img = img

        self.width, self.height = 150, 40
        self.color = (64, 64, 64)

        self.font = pygame.font.SysFont("consolas", 20)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):

        pygame.draw.rect(win, self.color, self.rect)
        pygame.draw.rect(win, self.color, pygame.Rect(self.x - 2, self.y - 2, self.width + 4, self.height + 4), 2, 2, 2, 2)

        if self.img is None:
            text = self.font.render(self.text, True, (255, 255, 255))
            win.blit(text, text.get_rect(center = self.rect.center))

        elif self.text is None:
            img = pygame.image.load(self.img)
            win.blit(img, img.get_rect(center = self.rect.center))
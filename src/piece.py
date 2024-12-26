import pygame

'''
KING - 0
PAWN - 1
BISHOP - 2
KNIGHT - 3
ROOK - 4
QUEEN - 5
'''

map = {0 : "K", 1 : "P", 2 : "B", 3 : "N", 4 : "R", 5 : "Q"}

black_map = {0 : "assets/pieces_new/black_king.png", 
             1 : "assets/pieces_new/black_pawn.png", 
             2 : "assets/pieces_new/black_bishop.png", 
             3 : "assets/pieces_new/black_knight.png", 
             4 : "assets/pieces_new/black_rook.png", 
             5 : "assets/pieces_new/black_queen.png"}

white_map = {0 : "assets/pieces_new/white_king.png", 
             1 : "assets/pieces_new/white_pawn.png", 
             2 : "assets/pieces_new/white_bishop.png", 
             3 : "assets/pieces_new/white_knight.png", 
             4 : "assets/pieces_new/white_rook.png", 
             5 : "assets/pieces_new/white_queen.png"}

class Piece:
    def __init__(self, x, y, value, color):
        self.x = x
        self.y = y
        self.value = value
        self.color = color

        self.notation = map[self.value] if self.color == 1 else map[self.value].lower()

        self.path = white_map[self.value] if self.color == 1 else black_map[self.value]
        self.img = pygame.image.load(self.path)

        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def draw(self, win):

        win.blit(self.img, self.img.get_rect(center = (self.x, self.y)))
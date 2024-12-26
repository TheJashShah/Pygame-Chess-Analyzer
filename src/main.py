import pygame
import pyperclip as pc

pygame.init()

from cell_list import make_list
from fen import parse_fen
from pgn_textfield import TextField
from PGN_to_FEN import PGN_TO_FEN
from stockfish_eval import get_stats
from eval_bar import EvalBar

from button import Button

class App:
    def __init__(self):
        self.width, self.height = 1200, 640
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (106, 106, 106)
        self.cell_list = make_list()

        self.textfield = TextField(740, 205)

        self.enter_btn = Button(self.textfield.rect.centerx - 75, self.textfield.rect.centery + 150, "Enter", None)
        self.back_btn = Button((680 + 220//3), 550, "Back", None)
        self.next_btn = Button(self.back_btn.x + self.back_btn.width + (220//3), 550, "Next", None)

        self.buttons = [self.enter_btn, self.back_btn, self.next_btn]

        self.move_tuples = None
        self.tuple_index = 0
        self.pair_index = 0

        self.EvalBar = EvalBar(0, 0, self.height)

        self.eval_score = 0
        self.top_moves = None
        self.font = pygame.font.SysFont("consolas", 20)

    def get_fen(self):

        with open("src/fen.txt", "r") as file:
            self.fen_list = file.readlines()

        self.fen_index = 0
        self.current_fen = self.fen_list[self.fen_index]
        self.piece_list = parse_fen(self.current_fen)

    def update(self):

        self.current_fen = self.fen_list[self.fen_index]
        self.piece_list = parse_fen(self.current_fen)
        self.handle_pieces()

    def handle_pieces(self):

        for i in range(8):
            for j in range(8):

                self.cell_list[i][j].previous = self.cell_list[i][j].piece
                self.cell_list[i][j].piece = self.piece_list[i][j]

    def parse_move(self, move_list):

        moves = {move['Move'] : move['Centipawn'] for move in move_list}

        return moves

    def display_moves(self):

        if self.top_moves is not None:

            text_list = []

            if self.fen_index % 2 == 0:
                label = "Best Move for White"
            else:
                label = "Best Move for Black"

            text = self.font.render(label, True, (255, 255, 255))
            self.win.blit(text, text.get_rect(center = (680 + (1200 - 680)/2, 50)))

            for item in self.top_moves:
                text_list.append(f"{item} : {self.top_moves[item]/100}")

            for idx, text in enumerate(text_list):
                TEXT = self.font.render(text, True, (255, 255, 255))
                self.win.blit(TEXT, TEXT.get_rect(center = ( 680 + (1200 - 680)/2, (75 + idx * 20))))

    def mark_change(self):

        for row in self.cell_list:
            for cell in row:

                if cell.previous != None and cell.piece != None:
                    if cell.previous.notation == cell.piece.notation:
                        cell.mask.set_alpha(0)
                        cell.mask_color = (255, 255, 255)
                    
                    else:
                        cell.mask.set_alpha(64)
                        cell.mask_color = (200, 200, 100)

                elif cell.previous is None and cell.piece is None:
                    cell.mask.set_alpha(0)
                    cell.mask_color = (255, 255, 255)

                else:
                    if self.current_fen != self.fen_list[0]:
                        cell.mask.set_alpha(64)
                        cell.mask_color = (200, 200, 100)

    def main_function(self):

        Running = True
        while Running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if self.textfield.rect.collidepoint(pos):
                        self.textfield.bg = (0, 0, 0)
                    else:
                        self.textfield.bg = (64, 64, 64)

                    if self.buttons[0].rect.collidepoint(pos):
                        self.move_tuples = PGN_TO_FEN(self.textfield.string)
                        self.get_fen()
                        self.handle_pieces()

                    if self.buttons[1].rect.collidepoint(pos):
                        
                        if self.fen_index > 0:
                            self.fen_index -= 1
                            self.update()
                            move, eval_score = get_stats(self.current_fen)
                            self.top_moves = self.parse_move(move)

                            self.eval_score = eval_score

                            self.EvalBar.change_bar(eval_score)

                    if self.buttons[2].rect.collidepoint(pos):

                        if self.fen_index < len(self.fen_list) - 1:
                            self.fen_index += 1
                            self.update()
                            move, eval_score = get_stats(self.current_fen)
                            self.top_moves = self.parse_move(move)

                            self.eval_score = eval_score

                            self.EvalBar.change_bar(eval_score)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        
                        if self.textfield.bg == (0, 0, 0):
                            self.textfield.display_string = pc.paste()
                            self.textfield.string = pc.paste()
            
            self.draw()

    def draw(self):

        self.win.fill(self.color)

        for row in self.cell_list:
            for cell in row:
                cell.draw(self.win)
            
        self.textfield.draw(self.win)

        for btn in self.buttons:
            btn.draw(self.win)

        self.mark_change()

        self.EvalBar.draw(self.win, self.eval_score)

        self.display_moves()

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()

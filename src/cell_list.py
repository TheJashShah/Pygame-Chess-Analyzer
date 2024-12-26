import pygame
from cell import Cell

def make_list():

    cell_list = [[0] * 8 for _ in range(8)]

    for i in range(8):
        for j in range(8):

            if (i + j) % 2 == 0:
                color = (177, 228, 185)
            else:
                color = (112, 162, 163)

            cell_list[i][j] = Cell((40 + (j * 80)), (0 + (i * 80)), color)

    return cell_list
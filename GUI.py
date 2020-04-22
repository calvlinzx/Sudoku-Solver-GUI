import time
import pygame
from solver import solve, valid

pygame.font.init()


class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    # Grid constructor
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.model = None
        self.selected = None


class Box:
    rows = 9
    cols = 9

    # Box constructor
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.tmp = 0
        self.selected = False

    # Set temporary value
    def set_tmp(self, val):
        self.tmp = val

    # Set value
    def set(self, val):
        self.value = val

    # Draw a tmp value on a certain box
    def draw(self, win):
        """
        param: window of the application
        """
        font = pygame.font.SysFont('comicsans', 40)
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        # if current box has tmp value but no final value
        if self.tmp != 0 and self.value == 0:
            text = font.render(str(self.tmp), True, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif self.value != 0:   # final value has been entered
            text = font.render(str(self.value), True, (0, 0, 0))
            win.blit(text, (x + gap/2 - text.get_width()/2, y + gap/2 - text.get_height()/2))

        # if current box is selected, it has red rectangle surrounded
        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

def main():
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption('Sudoku')

import time
import pygame
from solver import solve, valid
from box import *

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
        self.boxes = [[Box(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.model = None
        self.selected = None

    # update model
    def update_model(self):
        self.model = [[self.boxes[i][j].get_value() for j in range(self.cols)] for i in range(self.rows)]

    # place a value on a selected box
    def place_value(self, val):
        row, col = self.selected  # get row and col of selected box

        if self.boxes[row][col].get_value() == 0:  # no value has been placed
            self.boxes[row][col].set_value(val)  # set box value to val
            self.update_model()  # update model

            if valid(self.model, val, (row, col)):  # if value is valid for box
                return True
            else:
                self.boxes[row][col].set_value(0)  # set value back to 0
                self.boxes[row][col].set_tmp(0)  # set tmp back to 0
                self.update_model()  # update model
                return False

    # place a tmp value on a selected box
    def place_tmp(self, tmp):
        row, col = self.selected  # get row and col of selected box
        self.boxes[row][col].set_tmp(tmp)  # set tmp value to tmp

    # draw grid to a window
    def draw(self, win):
        gap = self.width / 9

        for i in range(1, self.rows + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            # draw horizontal lines
            pygame.draw.line(win, (0, 0, 0), (0, i*gap), (self.width, i*gap), thickness)
            # draw vertical lines
            pygame.draw.line(win, (0, 0, 0), (i*gap, 0), (i*gap, self.height), thickness)

        for i in range(self.rows):
            for j in range(self.cols):
                self.boxes[i][j].draw(win)


def main():
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption('Sudoku')


main()

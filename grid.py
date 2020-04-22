from solver import valid, solve
from box import *


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

    def get_selected(self):
        return self.selected

    # update model
    def update_model(self):
        self.model = [[self.boxes[i][j].get_value() for j in range(self.cols)] for i in range(self.rows)]

    # place a value on a selected box
    def place_value(self, val):
        row, col = self.selected  # get row and col of selected box

        if self.boxes[row][col].get_value() == 0:  # no value has been placed
            self.boxes[row][col].set_value(val)  # set box value to val
            self.update_model()  # update model

            if valid(self.model, val, (row, col)) and solve(self.model):  # if value is valid for box and solved
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

    # select a box with row and col
    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.boxes[i][j].selected = False

        self.boxes[row][col].selected = True
        self.selected = (row, col)

    # draw grid to a window
    def draw(self, win):
        gap = self.width / 9

        for i in range(1, self.rows + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            # draw horizontal lines
            pygame.draw.line(win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thickness)
            # draw vertical lines
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thickness)

        for i in range(self.rows):
            for j in range(self.cols):
                self.boxes[i][j].draw(win)

    # clear a selected box
    def clear(self):
        row, col = self.selected
        if self.boxes[row][col].get_value() == 0:
            self.boxes[row][col].set_tmp(0)

    # click a box
    def click(self, pos):
        """
        :param tuple (x, y)
        :return tuple (row, col)
        """
        x, y = pos[0], pos[1]

        if x < self.width and y < self.height:
            gap = self.width / 9
            row, col = x // gap, y // gap
            return int(row), int(col)
        else:
            return None

    # check if the grid is full
    def is_full(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.boxes[i][j].get_value() == 0:
                    return False
        return True

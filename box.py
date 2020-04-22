import pygame


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

    # Get value
    def get_value(self):
        return self.value

    # Set value
    def set_value(self, val):
        self.value = val

    # Draw a tmp value on a certain box
    def draw(self, win):
        """
        param: window of the application
        """
        font = pygame.font.SysFont('comicsans', 40)

        gap = self.width / 9    # get width/height of each box
        x = self.col * gap      # get current column
        y = self.row * gap      # get current row

        if self.tmp != 0 and self.value == 0:       # if current box has tmp value but no final value
            text = font.render(str(self.tmp), True, (128, 128, 128))  # render gray text of tmp value
            win.blit(text, (x + 5, y + 5))  # blit the text on top-left of current box
        elif self.value != 0:  # final value has been entered
            text = font.render(str(self.value), True, (0, 0, 0))  # render black text of final value
            win.blit(text, (x + gap / 2 - text.get_width() / 2, y + gap / 2 - text.get_height() / 2))  # blit on box

        # if current box is selected
        if self.selected:  # if current box is selected
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)  # surround box with red rectangle of width 3

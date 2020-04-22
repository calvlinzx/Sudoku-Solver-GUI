import time
import pygame
from solver import solve, valid
from box import *

pygame.font.init()


def main():
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption('Sudoku')


main()

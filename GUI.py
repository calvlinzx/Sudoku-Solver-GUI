import time
import pygame
from box import *
from grid import *

pygame.font.init()


# todo
def redraw_window(win, grid, timestamp, strikes):
    pass


# todo
def format_time(sec):
    pass


def main():
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption('Sudoku')
    grid = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0

    while run:
        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    grid.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = grid.get_selected()
                    if grid.boxes[i][j].tmp != 0:
                        if grid.place_value(grid.boxes[i][j].tmp):
                            print('Success')
                        else:
                            print('Wrong')
                            strikes += 1
                        key = None
                        if grid.is_full():
                            print('Game Over')
                            run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = grid.click(pos)
                if clicked:
                    grid.select(pos[0], pos[1])
                    key = None


main()
pygame.quit()

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
from typing import List


def visualize(board: List[List[int]]):
    """
    param: board
    """
    for i in range(len(board)):
        if i != 0 and i % 3 == 0:
            print('- - - - - - - - - - -')
        for j in range(len(board[0])):
            if j != 0 and j % 3 == 0:
                print('| ', end='')
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')


def findEmpty(board: List[List[int]]) -> tuple:
    """
    param: board
    return: tuple of position of empty box
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not board[i][j]:
                return i, j
    return None


def valid(board: List[List[int]], num: int, pos: tuple) -> bool:
    """
    param: board
    param: the number to be filled
    param: the position of the box to be filled in
    return: boolean
    """

    # Check rows
    for i in range(len(board[0])):
        if board[pos[0]][i] == num:  # and pos[1] != i:
            return False

    # Check columns
    for j in range(len(board)):
        if board[j][pos[1]] == num:  # and pos[0] != j:
            return False

    # Check 3*3 box
    box_y, box_x = pos[0] // 3, pos[1] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:  # and (i,j) != pos:
                return False
    return True


def solve(board: List[List[int]]) -> bool:
    """
    param: board
    return: bool
    """

    found = findEmpty(board)
    if not found:
        return True
    row, col = found

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            # Solve sub-problem by recursive call
            if solve(board):
                return True

            # Backtrack
            board[row][col] = 0
    return False


visualize(board)
print("\nSolving Sudoku...\n")
solve(board)
visualize(board)

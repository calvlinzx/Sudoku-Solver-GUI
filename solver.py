board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def visualize(board):
    for i in range(len(board)):
        if i != 0 and i % 3 == 0:
            print('- - - - - - - - - - -')
        for j in range(len(board[0])):
            if j != 0 and j % 3 == 0:
                print('| ', end = '')
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end = '')

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not board[i][j]:
                return (i,j)
    return None

visualize(board)
print(findEmpty(board))
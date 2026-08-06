n = int(input())

board = [[-1 for j in range(n)] for i in range(n)]

def solver(i, j, level):
    if i > n - 1:
        return
    if j > n - 1:
        return
    if i < 0:
        return
    if j < 0:
        return
    
    if level > 3 / 2 * n:
        return
    
    if board[i][j] != -1 and level > board[i][j]:
        return

    if board[i][j] == -1 or board[i][j] > level:
        board[i][j] = level

    solver(i + 2, j + 1, level + 1)
    solver(i + 1, j + 2, level + 1)
    solver(i - 1, j + 2, level + 1)
    solver(i - 2, j + 1, level + 1)
    solver(i + 1, j - 2, level + 1)
    solver(i + 2, j - 1, level + 1)
    solver(i - 2, j - 1, level + 1)
    solver(i - 1, j - 2, level + 1)

    return

solver(0, 0, 0)

for i in board:
    print(str(i).replace("[", "").replace("]", "").replace(",", ""))
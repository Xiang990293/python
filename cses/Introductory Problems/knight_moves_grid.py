from collections import deque

dirs_n = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (0, 1), (-1, 0)]
dirs_f = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (0, -1), (1, 0)]
dirs_o = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
dirs_d = [(1, 2), (-1, 2), (-2, 1), (-2, -1)]

def solver():
    waitq = deque([(0, 0)])
    while waitq:
        rr, cr = waitq.popleft()
        level = board[rr][cr] + 1
        
        if cr < rr:
            continue

        dirs = []
        
        dirs = dirs_d if cr == rr else (dirs_n if cr - rr == 1 else (dirs_f if cr - rr == 2 else dirs_o))
    
        for i in dirs:
            d, e = i
            r, c = rr+d, cr+e
            
            if r > c or c > n - 1 or r < 0 or c < 0:
                continue
            
            if board[r][c] != -1:
                continue

            waitq.append((r, c))
            board[r][c] = level
            board[c][r] = level

    return

n = int(input())
board = [[-1] * n for i in range(n)]
board[0][0] = 0
solver()
for i in board:
    print(" ".join(map(str, i)))
from collections import deque
import sys

def solver():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    board = [[-1] * n for i in range(n)]
    board[0][0] = 0
    dirs_n = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (0, 1), (-1, 0)]
    dirs_f = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (0, -1), (1, 0)]
    dirs_o = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    dirs_d = [(1, 2), (-1, 2), (-2, 1), (-2, -1)]
    dirs = [dirs_d, dirs_n, dirs_f, dirs_o]

    waitq = deque([(0, 0)])
    while waitq:
        rr, cr = waitq.popleft()
        level = board[rr][cr] + 1
        
        if cr < rr:
            continue

        opt = cr - rr
        if opt > 2:
            opt = 3
            
        for i in dirs[opt]:
            d, e = i
            r, c = rr+d, cr+e
            
            if r > c or c > n - 1 or r < 0 or c < 0:
                continue
            
            if board[r][c] != -1:
                continue

            waitq.append((r, c))
            board[r][c] = level
            board[c][r] = level

    
    output = []
    for row in board:
        output.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solver()
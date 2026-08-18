from collections import deque

n = int(input())

board = [[-1 for j in range(n)] for i in range(n)]
steped = set()
dirs_n = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (0, 1), (-1, 0)]
dirs_f = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (0, -1), (1, 0)]
dirs_o = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
dirs_d = [(1, 2), (-1, 2), (-2, 1), (-2, -1)]

def bfs(curl, level):
    """
        this return the non steped grid on the given "curl", 
        and put the level value on the current grid.

        curl contain three things:
            1. rr: row_recent
    """

    nextq = []
    rr, cr = curl

    if cr < rr:
        return nextq

    dirs = []

    dirs = dirs_d if cr == rr else (dirs_n if cr - rr == 1 else (dirs_f if cr - rr == 2 else dirs_o))

    for i in dirs:
        d, e = i
        r, c = rr+d, cr+e
        
        if r > c or c > n - 1 or r < 0 or c < 0:
            continue
        
        if (r, c) in steped:
            continue

        nextq.append((r, c))
        board[r][c] = level
        board[c][r] = level
        steped.add((r, c))
    
    return nextq

def solver():
    level = 1
    waitq = deque([(0, 0)])
    nextq = deque([])
    board[0][0] = 0
    steped.add((0, 0))

    while waitq:
        curl = waitq.popleft()
        
        nextq.extend(bfs(curl, level))

        if not waitq and nextq:
            waitq = nextq
            nextq = deque([])
            level += 1

    return

solver()

for i in board:
    print(str(i).replace("[", "").replace("]", "").replace(",", ""))
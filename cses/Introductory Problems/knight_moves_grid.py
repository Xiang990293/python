n = int(input())

board = [[-1 for j in range(n)] for i in range(n)]
steped = [[False for j in range(n)] for i in range(n)]
dirs_n = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (0, 1), (-1, 0)]
dirs_f = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (0, -1), (1, 0)]
dirs_o = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
dirs_d = [(1, 2), (-1, 2), (-2, 1), (-2, -1)]

def bfs(curl):
    waitq = []
    rr, cr, level, prev = curl

    if cr < rr:
        return waitq

    dirs = []

    dirs = dirs_d if cr == rr else (dirs_n if cr - rr == 1 else (dirs_f if cr - rr == 2 else dirs_o))

    # if prev != (0, 0):
    #     r, c = prev
    #     if (-r, -c) in dirs:
    #         dirs.remove((-r, -c))

    for i in dirs:
        d, e = i
        r, c = rr+d, cr+e
        
        if r > n - 1 or c > n - 1 or r < 0 or c < 0 or r > c:
            continue
        
        if steped[r][c]:
            continue
        waitq.append((r, c, level + 1, i))
        board[r][c] = level + 1
        board[c][r] = level + 1
        steped[r][c] = True
    
    return waitq

def solver():
    level = 1
    waitq = [(0, 0, 0, (0, 0))]
    board[0][0] = 0
    steped[0][0] = True

    while waitq:
        curl = waitq.pop(0)
        r, c, level, prev = curl
        
        waitq.extend(bfs(curl))
        # print(level)
        # for i in board:
        #     print(str(i).replace("[", "").replace("]", "").replace(",", ""))

    return

solver()

for i in board:
    print(str(i).replace("[", "").replace("]", "").replace(",", ""))
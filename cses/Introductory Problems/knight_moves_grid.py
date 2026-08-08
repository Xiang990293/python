n = int(input())

board = [[-1 for j in range(n)] for i in range(n)]
steped = [[False for j in range(n)] for i in range(n)]

def wfs(curl):
    waitq = []
    rr, cr, level = curl
    for i in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        d, e = i
        r, c = rr+d, cr+e
        
        if r > n - 1:
            continue
        if c > n - 1:
            continue
        if r < 0:
            continue
        if c < 0:
            continue
        
        if steped[r][c]:
            continue
        waitq.append((r, c, level + 1))
        board[r][c] = level + 1
        steped[r][c] = True
    
    return waitq

def solver():
    level = 1
    waitq = [(0, 0, 0)]
    board[0][0] = 0
    steped[0][0] = True

    while waitq:
        curl = waitq.pop(0)
        r, c, level = curl
        
        waitq.extend(wfs(curl))

    return

solver()

for i in board:
    print(str(i).replace("[", "").replace("]", "").replace(",", ""))
boarda = [
    input(),
    input(),
    input(),
    input(),
    input(),
    input(),
    input(),
    input()
]

r8 = range(8)

def solver(board, put):
    if put == 7:
        return int(find_first_available(board) is not None)
    
    count = 0
    coor = find_first_available(board)
    while coor != None:
        r, c = coor
        count += solver(reserver(board.copy(), r, c), put + 1)
        board[r] = board[r][:c] + "*" + board[r][c+1:]
        coor = find_first_available(board)
    
    return count
    
def reserver(board, r, c):
    diag1 = lambda y: y + c - r
    diag2 = lambda y: - y + c + r
    
    board[r] = "********"
    for j in r8:
        a = diag1(j)
        b = diag2(j)
        if a < 8 and a >= 0:
            board[j] = board[j][:a] + "*" + board[j][a+1:]
        if b < 8 and b >= 0:
            board[j] = board[j][:b] + "*" + board[j][b+1:]
        board[j] = board[j][:c] + "*" + board[j][c+1:]
                
    return board
    
def find_first_available(board):
    for i, r in enumerate(board):
        c = r.find(".")
        if c != -1:
            return i, c
            
    return None

print(solver(boarda, 0))

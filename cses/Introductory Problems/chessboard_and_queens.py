boarda = [
    int(input().replace(".", "1").replace("*", "0"), 2),
    int(input().replace(".", "1").replace("*", "0"), 2),
    int(input().replace(".", "1").replace("*", "0"), 2),
    int(input().replace(".", "1").replace("*", "0"), 2),
    int(input().replace(".", "1").replace("*", "0"), 2),
    int(input().replace(".", "1").replace("*", "0"), 2),
    int(input().replace(".", "1").replace("*", "0"), 2),
    int(input().replace(".", "1").replace("*", "0"), 2)
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
        board[r] &= 255 ^ 2**(7-c)
        coor = find_first_available(board)
    
    return count
    
def reserver(board, r, c):
    diag1 = lambda y: y + c - r
    diag2 = lambda y: - y + c + r
    
    board[r] = 0
    for j in r8:
        a = diag1(j)
        b = diag2(j)
        if a < 8 and a >= 0:
            board[j] &= 255 ^ 2**(7-a)
        if b < 8 and b >= 0:
            board[j] &= 255 ^ 2**(7-b)
        board[j] &= 255 ^ 2**(7-c)
                
    return board
    
    
def find_first_available(board):
    for i in r8:
        c = plog2(board[i])
        if c != -1:
            return i, int(c)
            
    return None

def plog2(d: int):
    if d == 0:
        return -1
    
    counter = 0
    filterd = 128
    while d & filterd == 0 and counter < 8:
        filterd >>= 1
        counter += 1
        
    return counter

print(solver(boarda, 0))

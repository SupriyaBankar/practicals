def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()
        
def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col]:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,n)):
        if board[i][j]:
            return False
    return True

def solve_n_queen_backtracking(board,row,n):
    if row==n:
        print_board(board)
        return True
    found_solution=False
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=True
            found_solution=solve_n_queen_backtracking(board,row+1,n) or found_solution
            board[row][col]=False
    return found_solution

def n_queen_backtracking(n):
    board=[[False]*n for _  in range(n)]
    if not solve_n_queen_backtracking(board,0,n):
        print("no solution exits")
    
    
n_queen_backtracking(4)
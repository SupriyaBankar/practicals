import math


MAX_PLAYER = 'x'   
MIN_PLAYER = 'o'   
EMPTY = '_'

class TicTacToe:
    def __init__(self):
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]
    
    def is_move_left(self, board):
        for row in board:
            if EMPTY in row:
                return True
        return False

    def evaluate(self, board):
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] and board[row][0] != EMPTY:
                return 10 if board[row][0] == MAX_PLAYER else -10

        for col in range(3):
            
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
                return 10 if board[0][col] == MAX_PLAYER else -10

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
            return 10 if board[0][0] == MAX_PLAYER else -10

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
            return 10 if board[0][2] == MAX_PLAYER else -10

        return 0  

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        score = self.evaluate(board)

       
        if score == 10:
            return score - depth 
        if score == -10:
            return score + depth 
        if not self.is_move_left(board):
            return 0 

        if is_maximizing:
            best = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = MAX_PLAYER  
                        best = max(best, self.minimax(board, depth + 1, False, alpha, beta))
                        board[i][j] = EMPTY  
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            break  
            return best

        else:
            best = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = MIN_PLAYER  
                        best = min(best, self.minimax(board, depth + 1, True, alpha, beta))
                        board[i][j] = EMPTY  
                        beta = min(beta, best)
                        if beta <= alpha:
                            break  
            return best

    def best_move(self):
        best_val = -math.inf
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = MAX_PLAYER 
                    move_val = self.minimax(self.board, 0, False, -math.inf, math.inf)
                    self.board[i][j] = EMPTY  

                    if move_val > best_val:
                        best_val = move_val
                        best_move = (i, j)
        return best_move

    def print_board(self):
      
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

game = TicTacToe()
game.board = [
    ['x', 'o', 'x'],
    ['o', 'o', '_'],
    ['_', '_', 'x']
]

print("Current board:")
game.print_board()

best_move = game.best_move()
print(f"\nThe best move for '{MAX_PLAYER}' is: {best_move}")

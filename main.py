import math

# Constants for the players
X = 'X'
O = 'O'
EMPTY = ' '

# Function to print the game board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the game is over
def game_over(board):
    return check_winner(board, X) or check_winner(board, O) or all(all(cell != EMPTY for cell in row) for row in board)

# Function to evaluate the game board
def evaluate(board):
    if check_winner(board, X):
        return 1
    if check_winner(board, O):
        return -1
    return 0

# Function to find the best move using minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if game_over(board) or depth == 0:
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = X
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval

    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = O
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI player
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = X
                eval = minimax(board, 9, alpha, beta, False)
                board[row][col] = EMPTY

                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)

    return best_move

# Function to play the game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = X

    while not game_over(board):
        if current_player == X:
            print("AI's turn:")
            row, col = find_best_move(board)
            board[row][col] = X
            print_board(board)
            print()

            if check_winner(board, X):
                print("AI wins!")
                break

            current_player = O
        else:
            print("Your turn:")
            valid_move = False

            while not valid_move:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))

                if board[row][col] == EMPTY:
                    board[row][col] = O
                    valid_move = True
                else:
                    print("Invalid move. Try again.")

            print_board(board)
            print()

            if check_winner(board, O):
                print("You win!")
                break

            current_player = X

    if not check_winner(board, X) and not check_winner(board, O):
        print("It's a draw!")

# Start the game
play_game()

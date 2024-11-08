import numpy as np

# Constants
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

# Functions to check for a win
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_O:
        return 1  # AI wins
    elif winner == PLAYER_X:
        return -1  # Player wins
    elif is_full(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    best_score = min(best_score, score)
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                score = minimax(board, 0, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (row, col)
    
    return move

# Print board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Main game loop
def main():
    board = np.full((3, 3), EMPTY)
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player X move
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] != EMPTY:
                print("Invalid move! Try again.")
                continue
            board[row][col] = PLAYER_X
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column as numbers between 0 and 2.")
            continue

        if check_winner(board) == PLAYER_X:
            print_board(board)
            print("Player X wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = find_best_move(board)
        if ai_move != (-1, -1):
            board[ai_move[0]][ai_move[1]] = PLAYER_O

        print_board(board)

        if check_winner(board) == PLAYER_O:
            print("Player O (AI) wins!")
            break
        
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()


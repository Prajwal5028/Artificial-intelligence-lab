def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def have_won(board, player):
    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        row, col = map(int, input(f"Player {player}, enter row and column: ").split())

        if board[row][col] == ' ':
            board[row][col] = player
            game_over = have_won(board, player)
            if game_over:
                print(f"Player {player} has won!")
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again!")

    print_board(board)


if __name__ == "__main__":
    main()

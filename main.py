def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player '{player}', enter row (0, 1, or 2): "))
        col = int(input(f"Player '{player}', enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print(f"Player '{player}' wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("That spot is already taken. Try again.")

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    play_game()

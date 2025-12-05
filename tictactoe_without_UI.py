def print_board(board: list[str]) -> None:
    """Print the current state of the Tic Tac Toe board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board: list[str], player: str) -> bool:
    """Return True if the given player has won."""
    winning_combos = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(
        board[a] == board[b] == board[c] == player for a, b, c in winning_combos
    )


def is_board_full(board: list[str]) -> bool:
    """Return True if there are no empty spaces left on the board."""
    return all(cell != " " for cell in board)


def get_player_move(board: list[str], player: str) -> int:
    """Ask the current player for a move and return the chosen position (0–8)."""
    while True:
        move = input(f"Player {player}, enter your move (1-9): ").strip()

        if not move.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        pos = int(move) - 1
        if pos < 0 or pos > 8:
            print("Invalid position. Choose a number between 1 and 9.")
            continue

        if board[pos] != " ":
            print("That spot is already taken. Choose another.")
            continue

        return pos


def play_game() -> None:
    """Play a single game of Tic Tac Toe."""
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered as follows:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board(board)
        move = get_player_move(board, current_player)
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


def main() -> None:
    """Main loop to play Tic Tac Toe, with an option to replay."""
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()



def print_board(board):
    """Print the Tic Tac Toe board"""
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")


def is_winner(board, player):
    """Check if the player has won"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False


def is_board_full(board):
    """Check if the board is full"""
    return all(cell != " " for row in board for cell in row)


def get_available_moves(board):
    """Get list of available moves"""
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves


def play_game():
    """Main game loop"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 0-8:")
    print(" 0 | 1 | 2")
    print("-----------")
    print(" 3 | 4 | 5")
    print("-----------")
    print(" 6 | 7 | 8")
    
    while True:
        print_board(board)
        
        # Get player move
        while True:
            try:
                position = int(input(f"Player {current_player}, enter position (0-8): "))
                row, col = divmod(position, 3)
                
                if position < 0 or position > 8:
                    print("Position must be between 0 and 8!")
                    continue
                
                if board[row][col] != " ":
                    print("That position is already taken!")
                    continue
                
                board[row][col] = current_player
                break
            except ValueError:
                print("Invalid input! Please enter a number between 0 and 8.")
        
        # Check for winner
        if is_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break
        
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"
    
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again in ["yes", "y"]:
        play_game()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    play_game()

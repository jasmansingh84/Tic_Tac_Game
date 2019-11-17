# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Display Board

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic tac toe
def play_game():
    # Show the initial game board
    display_board()


play_game()
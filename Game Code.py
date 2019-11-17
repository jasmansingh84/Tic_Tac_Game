# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_going = True

# Who is the winner
winner = None

# whos turn is it?
current_player = "X"

# Display Board

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic tac toe
def play_game():
    # Show the initial game board
    display_board()
# Loop until the game stops (winner or tie)
    while game_still_going:
        # Handle a turn
        handle_turn(current_player)

def handle_turn(player):

    position = input("Choose a position from 1-9: ")
    # Get correct index in our board list
    position = int(position) - 1

    board[position] = "X"
    display_board()

play_game()


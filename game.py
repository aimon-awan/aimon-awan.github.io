# Tic Tac Toe Game
# Created with Python3

# Start by making the board, 3 X 3 grid
board = [" " for i in range(9)]

# function to construct the board 
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2]) # first, second, third space
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5]) # fourth, fifth, sixth space
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8]) # seventh, eigth, ninth space

    print()  # blank line
    # Print Rows
    print(row1)
    print(row2)
    print(row3)
    print() # blank line

# This function will decide how the player will move
def player_move(icon):
    
    # if icon is "X" player is number 1
    if icon == "X":
        number = 1
    # else if icon is "O" player is number 2
    elif icon == "O":
        number = 2
        
    print("Your turn player {}".format(number))
    
    choice = int(input("Enter your move (1-9): ").strip())
    # Ask the player what move they would like to place

    # if the board has an empty space, then set the space to the icon
    if board[choice - 1] == " ":
        board[choice - 1] = icon

    # otherwise print a blank line and state that the space is taken    
    else:
        print()
        print("That space is taken!")

# This function will decide which player will win
def is_victory(icon):
    # Theres eight ways to win: getting all of row one, two, or three. 
    # All of column one, two, or three. Or getting the two diagonals.
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# This function will be called when theres no space left in the board
def is_draw():
    # if there is no space left in the board then there is a draw
    if " " not in board:
        return True
    else:
        return False
    
while True:
    print_board()
    player_move("X")
    print_board()
    # if X wins print statement and break
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    # else if there is a draw print statement and break    
    elif is_draw():
        print("its a draw!")
        break
    player_move("O")
    # if O wins print statement and break
    if is_victory("O"):
        print_board()
        print("O wins! Congratulations!")
        break
    # else if there is a draw print statement and break  
    elif is_draw():
        print("Its a draw!")
        break
    


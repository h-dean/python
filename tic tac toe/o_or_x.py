import random

########################
########  TODO  ########
########################
# clean 2 player code  #
# recursive win check  #
# make AI actually I   #
# detect 2 in a row    #
########################

### defining the board ###
board = [
    ["    1\t", "    2\t", "    3\t"],
    ["1", "\t", "\t", "\t"],
    ["2", "\t", "\t", "\t"],
    ["3", "\t", "\t", "\t"]]

### function to print board ###
def show_board():
    print("\n\n\n\n\n")
    print("\t\t", "".join(board[0]))
    print("\t\t",board[1][0], "|".join(board[1][1:]))
    print("\t\t","________________________")
    print("\t\t",board[2][0], "|".join(board[2][1:]))
    print("\t\t","________________________")
    print("\t\t",board[3][0], "|".join(board[3][1:]))
    print("\n\n\n\n\n")

### function to place letter on board ###
def put(x,y,char):
    if ("X" in board[y][x]) or ("O" in board[y][x]):
        return True
    else:
        board[y][x] = "  " + char + "\t"
        return False

### checking all win possibilities ###
def checkwin(char): 
    if (char in board[1][1]) and (char in board[2][1]) and (char in board[3][1]):
        return char, True
    if (char in board[1][2]) and (char in board[2][2]) and (char in board[3][2]):
        return char, True
    if (char in board[1][3]) and (char in board[2][3]) and (char in board[3][3]):
        return char, True
    if (char in board[1][1]) and (char in board[1][2]) and (char in board[1][3]):
        return char, True
    if (char in board[2][1]) and (char in board[2][2]) and (char in board[2][3]):
        return char, True
    if (char in board[3][1]) and (char in board[3][2]) and (char in board[3][3]):
        return char, True
    if (char in board[1][1]) and (char in board[2][2]) and (char in board[3][3]):
        return char, True
    if (char in board[1][3]) and (char in board[2][2]) and (char in board[3][1]):
        return char, True
    else:
        return False
    
#put(1, 1, "X")
#show_board()


### bunch of ai shit ###
def empty_spaces(board):
    empty = []
    for i, y in enumerate(board):
        for i0, x in enumerate(y):
            if x == "\t":
                empty.append([i0, i])
    return empty

def player_pos(board):
    positions = []
    for i, y in enumerate(board):
        for i0, x in enumerate(y):
            if "X" in x:
                positions.append([i0, i])
    return positions

def ai(choices, char):
    x, y = random.choice(choices)
    put(x, y, char)
    

### one player game function ###
def one_player_game():
    print("You are player X.")
    show_board()
    while (not checkwin("X")) and (not checkwin("O")):
        x, y = [int(x) for x in input("Enter the coords of where you want to go (x, y)").split(", ")]
        
        if not put(x, y, "X"):
            put(x, y, "X")
        else:
            print("That position is already taken, try again.")
            one_player_game()
            
        show_board()
        
        if checkwin("X"):
            print("You win!")
            break
        
        print("The computer has made its move.")
        empty = empty_spaces(board)
        ai(empty, "O")
        show_board()
        
        if checkwin("O"):
            print("You lose!")
            break
        
#one_player_game()

### main two player game function ###
def two_player_game():
    show_board()
    while (not checkwin("X")) and (not checkwin("O")):
        char = input("Are you X or O?").upper()

#        if char == "O":
#            char = "X"
#        else:
#            char = "O"
#        
#        print("It is player " + char + "'s turn")

        x, y = [int(x) for x in input("Enter the coords of where you want to go (x, y)").split(", ")]
        
        if not put(x, y, char):
            put(x, y, char)
        else:
            print("That position is already taken, try again")
            
            if char == "O":
                two_player_game()
            else:
                two_player_game()
                
            two_player_game()
            
        show_board()
        
    if checkwin("X"):
        print("Player X wins!")
        
    if checkwin("O"):
        print("Player O wins!")

#two_player_game()
#one_player_game()
players = input("Are you playing with a friend?").lower()
if players == "no":
    one_player_game()
else:
    two_player_game()


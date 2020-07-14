import random

# function which draws board
def drawboard(board):

    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])

# function which chooses randomly which player will go first
def chooseplayer():

    person_to_start = random.randint(0,1)

    if person_to_start == 1:
        print("The Computer will start first")
        return "computer"
    else:
        print("You will start first")
        return "player"

# function which allows player to choose which piece they want to be
def choosepiece():

    player_piece = ""

    while player_piece != "x" and player_piece != "o":
        player_piece = input("Please enter which piece you would like to be: x or o ")
        if player_piece != "x" and player_piece != "o":
            print("you have selected an invalid piece")
        else:
            break
    
    return player_piece

# function which allows player to input their choice for where they want to place their piece
def playerturn(board, player_piece):
    
    correct_guesses = [1,2,3,4,5,6,7,8,9]
    while " " in board:
        turn = input("Please input your turn, using 1-9 to select the box you want to choose ")
        turn = int(turn)
        if turn not in correct_guesses:
            print("Please enter a valid choice")
        elif board[turn] != " ":
            print("This space has already been taken, please choose another space")
        else:
            return turn

# function which makes the move on the actual board
def makemove(board,player_piece,move):
    board[move] = player_piece

# function which gets a copy of the board which allows us to make the computer moves
def getboardcopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

# function to make computer move, based on moves on the board
def cputurn(board, player_piece):
    
    if player_piece == "x":
        computer_piece = "o"
    else:
        computer_piece = "x"

    # computer can win in 1 turn
    for potential_turn in range(1,10):
        boardCopy = getboardcopy(board)
        if boardCopy[potential_turn] == " ":
            boardCopy[potential_turn] = computer_piece
            if checkcpuwin(boardCopy, computer_piece):
                return potential_turn
            else:
                boardCopy[potential_turn] = " " 
                potential_turn == 0
    
    # player can win in 1 turn and needs to be blocked
    for potential_turn in range(1,10):
        boardCopy = getboardcopy(board)
        if boardCopy[potential_turn] == " ":
            boardCopy[potential_turn] = player_piece
            if checkplayerwin(boardCopy, player_piece):
                return potential_turn
            else:
                boardCopy[potential_turn] = " " 
                potential_turn == 0

    # if any of the corner pieces are free, CPU will choose this
    for potential_turn in range(1,10,2):
        boardCopy = getboardcopy(board)
        if potential_turn == 5:
            continue
        elif boardCopy[potential_turn] == " ":
            return potential_turn
        else:
            boardCopy[potential_turn] = " "
            potential_turn = 0

    # if the middle spot is free, CPU will choose this
    for potential_turn in range(5):
        boardCopy =  getboardcopy(boardCopy)
        if boardCopy[potential_turn] == " ":
            return potential_turn
        else:
            boardCopy[potential_turn] = " "
            potential_turn = 0

    # if any of the side pieces are free, CPU will choose this
    for potential_turn in range(2,9,2):
        boardCopy =  getboardcopy(boardCopy)
        if boardCopy[potential_turn] == " ":
            return potential_turn
        else:
            print("There are no valid spaces for the Computer to choose")
            break           

# function which checks if the player has won
def checkplayerwin(board, player_piece):
    if (board[1] == player_piece and board[2] == player_piece and board[3] == player_piece) or (board[4] == player_piece and board[5] == player_piece and board[6] == player_piece) or (board[7] == player_piece and board[8] == player_piece and board[9] == player_piece) or (board[1] == player_piece and board[4] == player_piece and board[7] == player_piece) or (board[2] == player_piece and board[5] == player_piece and board[8] == player_piece) or (board[3] == player_piece and board[6] == player_piece and board[9] == player_piece) or (board[1] == player_piece and board[5] == player_piece and board[9] == player_piece) or (board[3] == player_piece and board[5] == player_piece and board[7] == player_piece):
        return True

# function which checks if the computer has won      
def checkcpuwin(board, computer_piece):
    if (board[1] == computer_piece and board[2] == computer_piece and board[3] == computer_piece) or (board[4] == computer_piece and board[5] == computer_piece and board[6] == computer_piece) or (board[7] == computer_piece and board[8] == computer_piece and board[9] == computer_piece) or (board[1] == computer_piece and board[4] == computer_piece and board[7] == computer_piece) or (board[2] == computer_piece and board[5] == computer_piece and board[8] == computer_piece) or (board[3] == computer_piece and board[6] == computer_piece and board[9] == computer_piece) or (board[1] == computer_piece and board[5] == computer_piece and board[9] == computer_piece) or (board[3] == computer_piece and board[5] == computer_piece and board[7] == computer_piece):
        return True    

# function which checks if the board is full, which symbolises a draw
def fullboard(board):
    if " " not in board:
        return True

def tictactoe():

    print("Welcome to Tic Tac Toe.")
    # prints board and sets condition of playing game to be true, to ensure we can loop through player and CPU's turn until there is a winner or a draw
    board = [""," "," "," "," "," "," "," "," "," ",]
    playing_game = True

    # sets variables equal to the function values for player piece and who's turn it is
    player_piece = choosepiece()
    turn = chooseplayer()

    if player_piece == "x":
        computer_piece = "o"
    else:
        computer_piece = "x"

    while playing_game == True:

        # if it's the player's turn, we draw the current board, allow the player to make their move and append move to the board
        if turn == "player":
            drawboard(board)
            playersgo = playerturn(board,player_piece)
            makemove(board,player_piece,playersgo)

            # checks to see if player has won or tied, and then breaks the playing game loop
            if checkplayerwin(board,player_piece):
                drawboard(board)
                print("You have won the game! Congratulations")
                playing_game = False
            else:
                if fullboard(board):
                    drawboard(board)
                    print("The Game is a Tie! Better luck next time!")
                    playing_game = False
                else:
                    #drawboard(board)
                    turn = "computer"
        # if its the CPU's turn, it get's the turn from the computer move function and makes that move to the board
        else:
            computersgo  = cputurn(board,player_piece)
            makemove(board, computer_piece,computersgo)

            if checkcpuwin(board,computer_piece):
                drawboard(board)
                print("You have lost the game! Bad Luck")
                playing_game = False
            else:
                if fullboard(board):
                    drawboard(board)
                    print("The Game is a Tie! Better luck next time!")
                    playing_game = False
                else:
                    #drawboard(board)
                    turn = "player"

tictactoe()

# V2 things to add:
# Player vs Player functionality
# Randomise CPU moves when they are placing pieces in the corners or sides
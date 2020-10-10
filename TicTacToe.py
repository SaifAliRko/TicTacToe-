
# we will be using a grid system to represent our board. To do this in python we will create a list called board that will start off with 10 empty values.

board = [' ' for x in range(10)]  # This should be the first line in your program
# board is now: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def insertLetter(letter,pos):
    board[pos] = letter
# This function is going to take two parameters: letter & pos. It is simply going to insert the given letter at the given position.
#  a letter here is X or O that  a player enters


def spaceIsFree(pos):
    return board[pos] == ' '

#  This function will return a True or False value
# This function will simply tell us if the given space is free. Meaning it does not already contain a letter.
# It has one parameter, pos, which will be an integer from 1-9


def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
# "board" is a list of 10 strings representing the board (ignore index 0)
# This function takes the board as a parameter and will display it to the console.

def isBoardFull(board):
    if board.count(' ') > 1:  # Since we always have one blank element in board we must use > 1
        return False
    else:
        return True
    # This function takes board as parameter and will simply return True if the board is full and False if it is not.



def IsWinner(b,l):
    # Given a board and a player’s letter, this function returns True if that player has won.
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

    # This function will tell us if the given letter has won based on the current board. It has two parameters: bo(board) & le(letter). The letter must be a “X” or an “O”.
    # We will simply check each possible winning line on the board and see if it is populated by the given letter.



# In this function we will be asking the user to input a move and validating it.
# If the move is valid we will add that letter to the board. Otherwise we will continue to ask the user for input.

def playerMove():
    run = True
    while run: # Keep looping until we get a valid move
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10: # makes sure we type in a number between 1-9
                if spaceIsFree(move):  # check if the move we choose is valid (no other letter is there already)
                    run = False        # to stop getting further input when its real one
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')

        except:
            print('Please type a number')




# making the computers move.
# It will examine the board and determine which move is the best to make.
def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ] # Create a list of possible moves , enumerate is a function
    move = 0

    # Check for possible winning move to take or to block opponents winning move
    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let      # now eg possibleMoves list was [1,2,3] boardcopy will be  O , O ,O (at 1,2,3) which leads to a winning move below
            if IsWinner(boardcopy, let):
                move = i                 # it will score the index which is winning either for computer or for if player wins by selecting that position
                return move


    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)     # Selects random indices of edges available
        return move

    if 5 in possibleMoves:     #take the centre position
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:           # try to take the otherwise edges
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

#This function will randomly decide on a move to take given a list of possible positions.
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)): # until board is not full
        if not(IsWinner(board , 'O')):  # and until the computer hasnt won
            playerMove()
            printBoard(board)
        else:
            print("sorry you loose!")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('computer placed an o on position' , move , ':')
                printBoard(board)
        else:
            print("you win!")
            break




    if isBoardFull(board):
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break

import random
import os

def clear():
    os.system( 'cls' )

def display_board(board):
    '''
    function that will print the board
    '''
    clear()
    newline = 3
    for ox in board :
        print(ox,'|',end = '')
        newline +=1
        if newline % 3 == 0:
            print('')

def player_input():
    '''
    function to determine the markers for the player , loops till a valid entry is entered
    '''
    player1_marker = input('Do you want to use X or O for player 1 ? ')
    if player1_marker == 'X':
        player2_marker = 'O'
        return [player1_marker,player2_marker]
    elif player1_marker == 'O':
        player2_marker = 'X'
        return [player1_marker,player2_marker]
    else :
        print('try again')
        player_input()

def free_space(board , position):
    '''
    function that returns a boolean indicating whether a space on the board is freely available.
    '''
    return board[position] == ' ' #the game starts with a board of spaces everywhere

def full_board(board):
    '''
    function that checks if the board is full and returns a boolean value. True if full, False otherwise.
    '''
    for i in range (0,9):
        if free_space(board,i):
            return False
            break
    else :
        return True

def assigning(board,marker,position):
    '''
    function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**
    '''
    board[position]=marker

def check_win(board,marker):
    '''
    checking if mark O or X has won the game
    '''
    for start in (0,3,6): #checking lines
        if board [start] == board [start +1] == board [start +2] == marker:
            return True
            break
    for start in (0,1,2): #checking columns
        if board[start] == board [start +3] == board [start +2*3] == marker:
            return True
            break
    if board [2] == board [4] == board [6] == marker:  #checking diago at positions (2,4,6):
        return True
    elif board[0] == board [4] == board [8] == marker:  #checking diago at positions (0,4,8)
        return True
    else:
        return False

def first_player ():
    '''
    returning randomly who starts first, 1 for player 1 and 2 for player 2
    '''
    return random.randint(1,2)

def next_position(board):
    '''
    function that asks for a player's next position (as a number 1-9) and
    check if it's a free position.
    If it is, then return the position for later use.
    '''
    while True :
        position = int(input("Please enter next move as a position 1 - 9 "))
        if free_space(board,position - 1):
            return position-1
            break
        else :
            print("that is already full , try again please, to help here's the board again")
            display_board(board)

def main_game():
    someone_won = False
    print ("Welcome to Tic Tac Toe Game !")
    markers = player_input()

    firsty=first_player() # this will be 1 if player 1 is first , and 2 is player 2 is first
    #markers is a list [player1_marker,player2_marker]
    #if firsty == 1 , no need to do anything since we start with markers[0] meaning player_1
    if firsty == 2:
        markers.reverse()
    print(f'{markers[0]} will start first')

    print("Here's your board : ")
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)

    while not (full_board(board) or someone_won):
        for play in range (0,2):
                print (f'it is {markers[play]} turn')  # [player1_marker,player2_marker]
                j = next_position(board)
                assigning(board,markers[play],j)
                display_board(board)
                if check_win(board,markers[play]):
                    print (f'{markers[play]} has won the game !')
                    someone_won = True
                    break

go_again = True
while go_again :
    main_game()
    again = input("would you like to go again ?  y/n")
    if again == "y":
        go_again = True
    else:
        go_again = False

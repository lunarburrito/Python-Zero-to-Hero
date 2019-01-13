#a function that can print out a board.
##Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**


def display_board(board):
    newline = 3
    for ox in board :
        print(ox,'|',end = '')
        newline +=1
        if newline % 3 == 0:
            print('')

def player_input():
    while True:
        player1_in = input('Do you want to use X or O for player 1')
        if player1_in == 'X':
            player2_in = 'O'
            break
        elif player1_in == 'O':
            player2_in = 'X'
            break
        else :
            print('try again')

#function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**
def assigning(board,marker,position):
    board[position-1]=marker

# checking if mark O or X has won the game
def check_win(board,marker):
    for start in range (0,7,3):
        for step in range (0,3):
                if board[start] == board[start+step] == board[start +2*step] == marker:
                    return True
                    break


print(check_win(['X','X','X','O','X','O','O','O','X'],'X'))
print(check_win(['O','X','X','X','X','X','O','O','X'],'X'))
print(check_win(['O','X','X','O','X','X','X','X','X'],'X'))
print(check_win(['O','X','X','O','X','O','X','X','X'],'X'))



#player_input()
#board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#display_board(board)
#print("testing assignement function X to position 2")
#assigning (board,'X',2)
#display_board(board)

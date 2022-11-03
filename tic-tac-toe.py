

'''
Author: Ndikum Sabastine Ndifor
Course: CSE210
Purpose: Program a Tic-Tac-Toe Game 
'''

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Great parti!") 

def create_board():
    '''This function creats a square grid containing 9 boxes'''
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    '''Displays the the square grid of 3 rows with each having 3 boxes
        row1 contains boxes 0,1,2
        row2 contains boxes 3,4,5
        row3 contains boxes 6,7,8
    '''
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_a_draw(board):
    '''Defines the conditions for a draw game and involves
    neither "Xs" nor "Os" not displaying the right way'''
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    '''Defines conditions for a win'''
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    '''Aks a player to start the game by choosing a number corresponding
    to a box and exclude the box for the next move for the next player not to be able to choose.
    Parameters: player,board
    return: nothing
    '''
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    '''Enhances the next player
        Parameter: current
        return "x" or "o"
        '''
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()
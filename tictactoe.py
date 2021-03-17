import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def init_board():
    board = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
    return board


def print_board(board):
    print("  1   2   3  ")
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" ---+---+---")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" ---+---+---")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}")
    print()


def check_winner_x(board):

    if board[0][0] == "X" and board[0][1] == 'X' and board[0][2] == 'X':
        return True
    if board[1][0] == "X" and board[1][1] == 'X' and board[1][2] == 'X':
        return True
    if board[2][0] == "X" and board[2][1] == 'X' and board[2][2] == 'X':
        return True
    if board[0][0] == "X" and board[1][0] == 'X' and board[2][0] == 'X':
        return True
    if board[0][1] == "X" and board[1][1] == 'X' and board[2][1] == 'X':
        return True
    if board[0][2] == "X" and board[1][2] == 'X' and board[2][2] == 'X':
        return True
    if board[2][0] == "X" and board[1][1] == 'X' and board[0][2] == 'X':
        return True
    if board[0][0] == "X" and board[1][1] == 'X' and board[2][2] == 'X':
        return True


def check_winner_0(board):

    if board[0][0] == "0" and board[0][1] == '0' and board[0][2] == '0':
        return True
    if board[1][0] == "0" and board[1][1] == '0' and board[1][2] == '0':
        return True
    if board[2][0] == "0" and board[2][1] == '0' and board[2][2] == '0':
        return True
    if board[0][0] == "0" and board[1][0] == '0' and board[2][0] == '0':
        return True
    if board[0][1] == "0" and board[1][1] == '0' and board[2][1] == '0':
        return True
    if board[0][2] == "0" and board[1][2] == '0' and board[2][2] == '0':
        return True
    if board[2][0] == "0" and board[1][1] == '0' and board[0][2] == '0':
        return True
    if board[0][0] == "0" and board[1][1] == '0' and board[2][2] == '0':
        return True


def full_board(board):
    count = 0

    for row in board:
        for col in row:
            if col != ".":
                count += 1
    
    if count == 9:
        return True

    return False

def get_position():
    pass

def choice(board):
    current_player = 1
    letters = ['A', 'B', 'C']
    numbers = ['1', '2', '3']
    i = '1'
    while i == '1':
        choice = input('Please place mark: ') #get position
        player_c = choice.upper()
        if len(player_c) == 2:
            row = letters.index(player_c[0])
            col = numbers.index(player_c[1])
            current_player += 1
            if current_player % 2 == 0:
                if board[row][col] == '.':
                    board[row][col] = 'X'
                else:
                    print('Not valid try again: ')
                    current_player -= 1
            else:
                if board[row][col] == '.':
                    board[row][col] = '0'
                else:
                    print('Not valid try again: ')
                    current_player -= 1
            if check_winner_x(board) == True:
                clear()
                print_board(board)
                print("\nX has won!")
                quit()
            if check_winner_0(board) == True:
                clear()
                print_board(board)
                print("\nO has won!")
                quit()
            
            if full_board(board) == True:
                clear()
                print_board(board)
                print('Game Over! It\'s a tie!')
                exit()
            clear()   
            print_board(board)
        elif player_c == 'QUIT':
            main_menu()
        else:
            print('Invalid, Pls try again')
            print_board(board)


def play():
    board = init_board()
    print_board(board)
    choice(board)


def greetings():
    print('Welcome to TICTACTOE Game \n Made by: Bence & Davies')


def main_menu():
    greetings()
    for i in range(4):
        time.sleep(1)
        print('...')

    print('\nMAIN MENU \n')
    print('(1) Human vs Human')
    mode = input('please choose game mode: ')
    if mode == '1':
        clear()
        play()


if __name__ == '__main__':
    main_menu()


#has_won

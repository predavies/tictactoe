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


def choice():
    current_player = 1
    letters = ['A', 'B', 'C']
    numbers = ['1', '2', '3']
    i = '1'
    while i == '1':
        choice = input('Please place mark: ')
        player_c = choice.upper()
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
            
        
        print_board(board)


board = init_board()
print_board(board)
choice()

#has_won

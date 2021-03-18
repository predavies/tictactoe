import os
import time
import random


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



def is_input_invalid(board, move, letters, numbers): # itt meg vizsgálja hogy  az input 2 nél nagyobb vagy benne van a listába ha nem vissza dob
    if len(move) == 2:
        if move[0] in letters and move[1] in numbers:
            return True
        elif move == 'QUIT':
            quit()
    return False    


def player_input(board):
    letters = ['A', 'B', 'C']
    numbers = ['1', '2', '3']

    move = input(f'Please place mark: {letters} {numbers} ').upper()  # átalakítottam ki raktam a vizsgálatát 
    while not is_input_invalid(board, move, letters, numbers):
        if move == 'QUIT':
            quit()
        move = input(f'Please place mark: {letters} {numbers} ').upper()

    row = letters.index(move[0])
    col = numbers.index(move[1])
    board[row][col] = 'X'
    print_board(board)
    time.sleep(1)
    if full_board(board) == False:
        ai_move(board, move) 

    return move


def ai_move(board, move):
    letters = ['A', 'B', 'C']
    numbers = ['1', '2', '3']

    ai_choice_row = random.choice(letters)
    ai_choice_col = random.choice(numbers)
            

    ai_choice = ai_choice_row + ai_choice_col

    row = letters.index(ai_choice[0])
        
    col = numbers.index(ai_choice[1])
            
    if ai_choice != move and board[row][col] == '.': # ciklus, lista
        board[row][col] = '0'

    else: 
        ai_move(board, move)


def choice(board):
    current_player = 1
    letters = ['A', 'B', 'C']
    numbers = ['1', '2', '3']
    i = '1'
    while i == '1':
        move = input(f'Please place mark: {letters} {numbers} ').upper()  # átalakítottam ki raktam a vizsgálatát 
        while not is_input_invalid(board, move, letters, numbers):
            if move == 'QUIT':
                quit()
            move = input(f'Please place mark: {letters} {numbers} ').upper()
            
        row = letters.index(move[0])
        col = numbers.index(move[1])
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
        

def play():
    board = init_board()
    print_board(board)
    choice(board)


def play2():
    board = init_board()
    print_board(board)
    p = 't'
    while p == 't':
        move = player_input(board)
        check_winner_0(board)
        check_winner_x(board)
        full_board(board)
        clear()
        print_board(board)

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
    


def greetings():
    print('Welcome to TICTACTOE Game \n Made by: Bence & Davies')


def main_menu():
    greetings()
    for i in range(4):
        time.sleep(1)
        print('...')
    print('\nMAIN MENU \n')
    print('(1) Human vs Human')
    print('(2) Human vs AI')
    mode = input("Chose a level\n")                   
    while mode not in ["1", "2"]:
        print(f"{mode} is not eligible!")
        mode = input("Chose a level\n")  
    if mode == '1':
        clear()
        play()
    if mode == '2':
        clear()
        play2()
    



if __name__ == '__main__':
    main_menu()



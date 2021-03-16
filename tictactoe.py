import os

def init_board():
    board = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
    return board


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    print("  1   2   3  ")
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" ---+---+---")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" ---+---+---")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}")
    print()

def is_valid(board, player_c, letters, numbers):
    if len(player_c) == 2:
        if player_c[0] in letters and player_c[1] in numbers:
            return True
    elif player_c == 'QUIT':
        clear()
        print('Csőváz')
        exit()
    else:
        return False


def player_choice(board):
    choice = input('Please place mark: ')
    player_c = choice.upper()
    letters = ['A', 'B', 'C']
    numbers = ['1', '2', '3']

    while is_valid(board, player_c, letters, numbers) != True:
        player_choice(board)

    row = letters.index(player_c[0])
    col = numbers.index(player_c[1])
    board[row][col] = 'X'
    clear()
    print_board(board)

    return player_c

def main():  
    i = '1' 
    board = init_board()
    print_board(board)
    while i == '1':
        player_choice(board)
if __name__ == '__main__':
    main()
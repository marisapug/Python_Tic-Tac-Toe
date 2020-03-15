import numpy as np
import random

def setup_board(n):
    board = [[None] * n for i in range(n)]
    count = 1
    for i in range(n):
        for j in range(n):
            board[i][j] = count
            count += 1
    return board

class Board:
    
    def __init__(self, n):
        self.dim = n
        self.board = setup_board(n)

    def display_board(self):
        for my_list in self.board:
            string_to_print = ""
            for x in my_list:
                string_to_print = string_to_print + str(x) + "     "
            print(string_to_print)

    def make_move(self, x, move):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == x:
                    self.board[i][j] = move


    def check_horizontal(self):
        strings = []
        for i in range(0, self.dim):
            string = ""
            for j in range (0, self.dim):
                string = string + str(self.board[i][j])
            strings.append(string)
        x_string = ""
        o_string = ""
        for x in range(0, self.dim):
            x_string = x_string + "x"
            o_string = o_string + "o"
        if x_string in strings:
            print("You win!")
        if o_string in strings:
            print("I win! You lose!")
        else:
            return False


    def check_vertical(self):
        strings = []
        for i in range(0, self.dim):
            string = ""
            for j in range (0, self.dim):
                string = string + str(self.board[j][i])
            strings.append(string)
        x_string = ""
        o_string = ""
        for x in range(0, self.dim):
            x_string = x_string + "x"
            o_string = o_string + "o"
        if x_string in strings:
            print("You win!")
        if o_string in strings:
            print("I win! You lose!")
        else:
            return False


    def check_diagnol(self):
        left_diag = ""
        right_diag = ""
        x = 0
        y = 0
        for i in range(0, self.dim):
            left_diag = left_diag + str(self.board[x][y])
            x = x + 1
            y = y + 1
        x = self.dim - 1
        y = 0
        for i in range(0, self.dim):
            right_diag = right_diag + str(self.board[x][y])
            x = x - 1
            y = y + 1
        strings = []
        strings.append(left_diag)
        strings.append(right_diag)
        x_string = ""
        o_string = ""
        for x in range(0, self.dim):
            x_string = x_string + "x"
            o_string = o_string + "o"
        if x_string in strings:
            print("You win!")
        if o_string in strings:
            print("I win! You lose!")
        else:
            return False


    def has_won(self):
        return (self.check_horizontal() or self.check_vertical() or self.check_diagnol())

    def make_computer_move(self):
        x = np.random.randint(self.dim)
        y = np.random.randint(self.dim)
        while self.board[x][y] is 'x':
            x = np.random.randint(self.dim)
            y = np.random.randint(self.dim)
        self.board[x][y] = 'o'


board = Board(3)
board.display_board()
while not board.has_won():
    x = int(input("Make your move by picking a number"))
    board.make_move(x, 'x')
    board.display_board
    if not board.has_won():
        print("Here I go . . ")
        board.make_computer_move()
        board.display_board()
    else:
        print('You won!')




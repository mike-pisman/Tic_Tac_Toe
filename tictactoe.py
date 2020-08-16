# Mikhail Pisman
# https://github.com/mike-pisman/Tic_Tac_Toe
# Tic-Tac-Toe
# Game class and main

import re
import random


class TicTacToe:
    def __init__(self, p1, p2):
        self.board = [None] * 9
        self.turn = True  # True - player, False - computer
        self.player = [p1, p2]
        self.player_turn = 0
        # while True:
        # self.board = input("Enter cells: > ").strip()

        '''if re.match(r'^[_XO]{9}$', self.board):
            self.board = list(self.board.replace('_', None))
            self.turn = 'X' if self.board.count('X') == self.board.count('O') else 'O'
            break
        else:
            print("Please enter 9 character string resembling the board, only 'X', 'O', or '_' chars are allowed")
        '''

    def print_board(self):
        print('-' * 9)
        for j in range(3):
            print('| ', end="")
            for k in range(3):
                e = self.board[j*3 + k]
                if e == True:
                    print('X ', end="")
                if e == False:
                    print('O ', end="")
                if e is None:
                    print('  ', end="")
            print('|')
        print('-' * 9)

    def check_game(self):
        for i in range(3):
            # Check row
            l = self.board[(i * 3):(i*3 + 3)]
            if all(e == l[0] and e is not None for e in l):
                self.print_win_msg(l[0])
                return True
            # Check column
            l = self.board[i:(i + 7):3]
            if all(e == l[0] and e is not None for e in l):
                self.print_win_msg(l[0])
                return True
        # Check diagonal
        if self.board[0] == self.board[4] == self.board[8] is not None:
            self.print_win_msg(self.board[0])
            return True
        # Check other diagonal
        if self.board[2] == self.board[4] == self.board[6] is not None:
            self.print_win_msg(self.board[2])
            return True
        # If no more cells left and no winner
        if None not in self.board:
            print('Draw')
            return True
        # print('Game not finished')
        return False

    def print_win_msg(self, who):
        print('X wins' if who else 'O wins')

    def check_cell(self, x, y):
        return self.board[(x - 1) + (3 - y) * 3] is None

    def set_cell(self, x, y, value):
        self.board[(x - 1) + (3 - y) * 3] = value

    def computer_move(self):
        while True:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            if self.check_cell(x, y):
                print('Making move level "{}"'.format(self.player[self.player_turn]))
                self.set_cell(x, y, self.turn)
                break

    def player_move(self):
        def check_input(a):
            if not a.isdigit():
                print("You should enter numbers!")
                return False
            if not int(a) in range(1, 4):
                print("Coordinates should be from 1 to 3!")
                return False
            return True

        while True:
            l = input("Enter the coordinates: > ").strip().split()
            if all(map(check_input, l)):
                if len(l) == 2:
                    x, y = map(int, l)
                    if self.check_cell(x, y):
                        self.set_cell(x, y, self.turn)
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Please enter only two values separated by a single space")

    def next_move(self):
        turn = self.player[self.player_turn]
        if turn == "user":
            self.player_move()
        if turn == "easy":
            self.computer_move()
        self.player_turn = not self.player_turn
        self.turn = not self.turn


def main():
    while True:
        command = input("Input command: > ").strip().split()
        if len(command) == 3:
            if command[0] == "start":
                if (command[1] == "user" or command[1] == "easy") and (command[2] == "user" or command[2] == "easy"):
                    game = TicTacToe(command[1], command[2])
                    game.print_board()
                    while True:
                        game.next_move()
                        game.print_board()
                        if game.check_game():
                            break
                else:
                    print("Bad parameters!")
        if command[0] == "exit":
            break




if __name__ == '__main__':
    main()

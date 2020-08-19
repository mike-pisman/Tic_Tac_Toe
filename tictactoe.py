# Mikhail Pisman
# https://github.com/mike-pisman/Tic_Tac_Toe
# Tic-Tac-Toe
# Game class and main

import re
import random


class TicTacToe:
    def __init__(self, p1, p2):
        self.board = [None] * 9
        self.turn = True  # False - p1, True - p2 first move
        self.player = [p2, p1]

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

    def check_game(self, print_value, board = None):
        if board == None:
            board = self.board
        for i in range(3):
            # Check row
            l = board[(i * 3):(i*3 + 3)]
            if all(e == l[0] and e is not None for e in l):
                if print_value:
                    self.print_win_msg(l[0])
                return True
            # Check column
            l = board[i:(i + 7):3]
            if all(e == l[0] and e is not None for e in l):
                if print_value:
                    self.print_win_msg(l[0])
                return True
        # Check diagonal
        if board[0] == board[4] == board[8] is not None:
            if print_value:
                self.print_win_msg(board[0])
            return True
        # Check other diagonal
        if board[2] == board[4] == board[6] is not None:
            if print_value:
                self.print_win_msg(board[2])
            return True
        # If no more cells left and no winner
        if None not in board:
            if print_value:
                print('Draw')
            return False
        return None
        # print('Game not finished')

    def print_win_msg(self, who):
        print('X wins' if who else 'O wins')

    def check_cell(self, x, y):
        return self.board[(x - 1) + (3 - y) * 3] is None

    def set_cell(self, x, y, value):
        self.board[(x - 1) + (3 - y) * 3] = value

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

    def easy_move(self):
        while True:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            if self.check_cell(x, y):
                #print('Making move level "{}"'.format(self.player[self.turn]))
                self.set_cell(x, y, self.turn)
                break

    def medium_move(self):
        for x in range(1, 4):
            for y in range(1, 4):
                if self.check_cell(x, y):
                    self.set_cell(x, y, self.turn)
                    if self.check_game(False):
                        print('Making move level "{}"'.format(self.player[self.turn]))
                        return
                    self.set_cell(x, y, None)

        for x in range(1, 4):
            for y in range(1, 4):
                if self.check_cell(x, y):
                    self.set_cell(x, y, not self.turn)
                    if self.check_game(False):
                        self.set_cell(x, y, self.turn)
                        print('Making move level "{}"'.format(self.player[self.turn]))
                        return
                    self.set_cell(x, y, None)
        self.easy_move()

    def hard_move(self):
        def minimax(board, turn):
            new_turn = turn
            new_board = board[:]
            moves = []

            check = self.check_game(False, new_board)
            if check is True:
                return (-1, 10) if self.turn == new_turn else (-1, -10)
            if check is False:
                return (-1, 0)

            for i in range(9):
                if new_board[i] is None:
                    new_board[i] = new_turn
                    score = minimax(new_board, not new_turn)[1]
                    new_board[i] = None
                    moves.append((i, score))

            if self.turn == new_turn:
                best_score = 10000
                for move in moves:
                    if move[1] < best_score:
                        best_score = move[1]
                        best_move = move
            else:
                best_score = -10000
                for move in moves:
                    if move[1] > best_score:
                        best_score = move[1]
                        best_move = move

            return best_move

        best_move = minimax(self.board, self.turn)

        #print('Making move level "hard"')
        self.board[best_move[0]] = self.turn

    def next_move(self):
        turn = self.player[self.turn]
        if turn == "user":
            self.player_move()
        if turn == "easy":
            self.easy_move()
        if turn == "medium":
            self.medium_move()
        if turn == "hard":
            self.hard_move()
        self.turn = not self.turn

def main():
    while True:
        available_commands = ["user", "easy", "medium", "hard"]
        command = input("Input command: > ").strip().split()
        if len(command) == 3:
            if command[0] == "start":
                if (command[1] in available_commands) and (command[2] in available_commands):
                    game = TicTacToe(command[1], command[2])
                    game.print_board()
                    while True:
                        game.next_move()
                        Harp option fixedgame.print_board()
                        if game.check_game(True) is not None:
                            break
                else:
                    print("Bad parameters!")
        if command[0] == "exit":
            break

if __name__ == '__main__':
    main()

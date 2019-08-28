import numpy as np
import os
import time

class Game:
    def __init__(self):
        self.remaining_moves = [i for i in range(0 , 9)]
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        cls = os.system('cls')
        for i in [0,3,6]:
            print( ' ' , self.board[i], ' | ' , self.board[i+1] , ' | ' , self.board[i+2])

    def get_state(self):
        return tuple(self.board)

    def get_possible_actions(self):
        return self.remaining_moves
    
    def reset(self):
        self.remaining_moves = [i for i in range(0 , 9)]
        self.board = [' ' for _ in range(9)]

    def check(self):
        #checking rows..
        for i in [0,3,6]:
            if self.board[i] == self.board[i+1] and self.board[i] == self.board[i+2]:
                if self.board[i] != ' ':
                    #print('Row' , self.board[i])
                    return 1
        #checking cols
        for i in [0 , 1 , 2]:
            if self.board[i] == self.board[i+3] and self.board[i] == self.board[i+6]:
                if self.board[i] != ' ':
                    #print('Cols' ,self.board[i])
                    return 1
        
        if self.board[0] == self.board[4] and self.board[0] == self.board[8]:
            if self.board[4] != ' ':
                #print('X' , self.board[4])
                return 1
        if self.board[2] == self.board[4] and self.board[2] == self.board[6]:
            if self.board[4] != ' ':
                #print('Z' , self.board[4])
                return 1
        
        return 0


    def perform_move(self , move , player):
        if move in self.remaining_moves:
            self.remaining_moves.remove(move)
            self.board[move] = player
            won = self.check()
            if won == 0 and len(self.remaining_moves) == 0:
                #print('TIE')
                return 0.5
            return won
    
if __name__ == "__main__":
    g = Game()
    for i in range(9):
        x = int(input())
        print(g.perform_move(x , 'X'))
        g.print_board()

        
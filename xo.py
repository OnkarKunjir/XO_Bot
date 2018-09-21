import numpy as np 
import os
import copy
class game:
    board = None
    remaining = None
    
    def __init__(self):
        self.board = {1:'-' , 2: '-' , 3: '-' ,4:'-' , 5:'-' , 6: '-' , 7: '-' ,8:'-' , 9:'-'}
        self.remaining = [i for i in range(1,10)] 

    def cls(self):
        c = os.system('cls')

    def update(self):
        self.cls()
        print(self.remaining)
        print(self.board[1] , ' | ' , self.board[2] ,' | ', self.board[3])
        print(self.board[4] , ' | ' , self.board[5] ,' | ', self.board[6])
        print(self.board[7] , ' | ' , self.board[8] ,' | ', self.board[9])

    def result(self , new_board):
        if(new_board[1]==new_board[2]==new_board[3] == 'X' or new_board[4]==new_board[5]==new_board[6] == 'X' or new_board[7]==new_board[8]==new_board[9]=='X' or new_board[1]==new_board[4]==new_board[7]=='X' or
        new_board[2]==new_board[5]==new_board[8]=='X' or new_board[3]==new_board[6]==new_board[9]=='X' or
        new_board[1]==new_board[5]==new_board[9]=='X' or new_board[3]==new_board[5]==new_board[7]=='X'):
            return -10
        else:
            return +10

    def play(self , is_new = True):
        move = None 
        if is_new:
            move = int(input('Play your move :- '))
        else:
            move = int(input('Enter the block number which is not occupied :- '))
        print(self.board[move])
        if self.board[move] == '-':
            self.board[move] = 'X'
            self.remaining.remove(move)
        else:
            self.play(is_new = False)
        self.bot(self.board)
        self.update()
        print(self.result(new_board = self.board))

    def one_move_p_win(self , new_board):
        for i in self.remaining:
            cpy = copy.copy(new_board)
            cpy[i] = 'X'
            res = self.result(cpy)
            if res == -10:
                return True,i
        return False , 0

    def one_move_p_lose(self , new_board):
        for i in self.remaining:
            cpy = copy.copy(new_board)
            cpy[i] = 'O'
            if(cpy[1] == cpy[2] == cpy[3] == 'O' or cpy[4] == cpy[5] == cpy[6] == 'O' or cpy[7] == cpy[8] == cpy[9] == 'O' or
               cpy[1] == cpy[4] == cpy[7] == 'O' or cpy[2] == cpy[5] == cpy[8] == 'O' or cpy[3] == cpy[6] == cpy[9] == 'O' or
               cpy[1] == cpy[5] == cpy[9] == 'O' or cpy[3] == cpy[5] == cpy[6] == 'O'):
                return True , i
        return False , 0

    def bot(self , new_board):
        p_win , p_win_mov = self.one_move_p_win(new_board)
        p_lose , p_lose_mov = self.one_move_p_lose(new_board)
        if p_win:
            self.board[p_win_mov] = 'O'
            self.remaining.remove(p_win_mov)
            return True
        elif p_lose:
            self.board[p_lose_mov] = 'O'
            self.remaining.remove(p_lose_mov)
            return True
        else:
            mov = self.remaining[0]
            self.board[mov] = 'O'
            self.remaining.remove(mov)
            return True

        

g = game()
g.update()
for i in range(9):
    g.play()
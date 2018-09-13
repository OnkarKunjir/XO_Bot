import numpy as np 
import pandas as pd 
import os 

class xo:
    env = np.zeros([3,3])
    remaining = None
    #constructio
    def __init__(self):
        self.remaining = 9
        self.cls()
        print(self.env)
    #clear
    def cls(self):
        x = os.system('cls')
    
    #display updated env
    def update(self):
        #self.cls()
        print(self.env)

    def check(self, envcpy):
        win = False
        party = 0

        for i in range(3):
            if envcpy[i , 0] == envcpy[i , 1] == envcpy[i , 2]  and envcpy[i ,i ] != 0:
                win = True
                party = envcpy[i , i]
                break

            elif envcpy[0 , i] == envcpy[1 , i] == envcpy[2 , i] and envcpy[i ,i ] != 0:
                win = True
                party = envcpy[i , i]
                break

        if envcpy[0 , 0] == envcpy[1 , 1] == envcpy[2 , 2] and envcpy[i ,i] != 0:
                win = True
                party = envcpy[i , i]
       
        elif envcpy[0 , 2] == envcpy[1 , 1] == envcpy[2 , 0] and envcpy[i ,i] != 0:
                win = True
                party = envcpy[i , i]
        
        
        if win:
            if party == 1:
                return 1
            else:
                return -1
        else:
            return None

    def play(self):
        if self.remaining > 0:
            x = int(input('row :- '))
            y = int(input('column:- '))
            if self.env[x-1 , y-1] == 0:
                self.env[x-1,y-1] = 1
                self.remaining -= 1
                win = self.check(self.env)
                if win == 1:
                    print(' !!! YOU WON THE MATCH !!! ')
                else:
                    bx , by = self.bot()
                    self.remaining -= 1
                    self.env[bx , by] = 2
            self.update()
            win = self.check(self.env)
            if win == -1:
                print(' !!! YOU LOSE THE MATCH !!! ')
            


    def bot(self):
        x_mov , y_mov = [] , []
        envcpy = np.copy(self.env)
        rmcpy = 0
        rmcpy = np.copy(self.remaining)
        switch = 2

        win = False
        while not(win):
            while rmcpy > 0:
                np.random.seed()
                rand = np.random.randint(0 ,9)
                x = int(rand/3)
                y = int(rand%3)
                if envcpy[x,y] == 0:
                    rmcpy -= 1
                    x_mov.append(x)
                    y_mov.append(y)
                    if switch == 2:
                        envcpy[x,y] = 2
                        switch = 1
                    else:
                        envcpy[x,y] = 1
                        switch = 2
                #print(envcpy)
            bwin = self.check(envcpy)
            if(bwin == -1):
                win = True
                print('win sit')
                return x_mov[0] ,y_mov[0]
            else:
                #print(envcpy)
                envcpy = np.copy(self.env)
                rmcpy = 0
                rmcpy = np.copy(self.remaining)
                x_mov , y_mov = [] ,[]
            

         
game = xo()
proceed = True
game.bot()
while proceed:
    game.play()
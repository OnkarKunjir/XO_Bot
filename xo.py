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
                self.env[x-1,y-1] = input()
                self.remaining -= 1
                self.update()
            print(self.check(self.env))
            

           

    def bot(self):
        x_mov , y_mov = [] , []
        envcpy = np.copy(self.env)
        rmcpy = np.copy(self.remaining)
        switch = 2

        win = False
        while not(win):
            while rmcpy > 0:
                x , y = np.random.randint(0 , 3) , np.random.randint(0,3)
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
                print(envcpy)
            bwin = self.check(envcpy)
            if(bwin == -1):
                win = True
                return x_mov[0] ,y_mov[0]
            else:
                envcpy = np.copy(self.env)
                rmcpy = np.copy(self.remaining)
                x_mov , y_mov = [] ,[]

         
                    
                
                    

game = xo()
proceed = True
game.bot()
while proceed:
    game.play()
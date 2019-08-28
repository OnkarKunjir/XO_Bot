import game 
import numpy as np 
import time
from tqdm import tqdm

EPISILON = 0.2
GAMMA = 0.9
TOTAL_WIN = 0
EPISODES = 10000
g = game.Game()



def get_epsilon_action(a,e=0):
    if np.random.random() < e:
        return np.random.choice(g.get_possible_actions())
    return a 

def add_state(policy , Q , returns):
    policy[g.get_state()] = np.random.choice(g.get_possible_actions())
    Q[g.get_state()] = {i:0  for i in range(0 , 9)}
    for i in range(9):
        returns[(g.get_state() , i)] = []
    

def play_episode(policy , Q , returns):
    if g.get_state() not in policy.keys():
        add_state(policy , Q , returns)

    a = get_epsilon_action(policy[g.get_state()] , EPISILON)
    state_action_rewards = [(g.get_state() , a , 0)]

    while True:
        #print('pa a' , g.get_possible_actions() , a)
        r = g.perform_move(a , 'X')
        
        #g.print_board()
        if r != 0:
            #print('B1')
            state_action_rewards.append((g.get_state() , None , r))
            #TOTAL_WIN += 1
            break
        #now apponent will play random action
        r = g.perform_move(np.random.choice(g.get_possible_actions()) , 'O')
        if r != 0:
            if r == 1:
                #if opponent won then give -ve reward
                r = -1
            state_action_rewards.append((g.get_state() , None , r))
            break
        

        if g.get_state() not in policy.keys():
            add_state(policy , Q , returns)
        a = get_epsilon_action(policy[g.get_state()] , EPISILON)
        state_action_rewards.append((g.get_state() , a , r))
        
    state_action_rewards.reverse()
    state_action_returns = []
    G = 0
    first = True 
    
    for s , a , r in state_action_rewards:
        if first:
            first = False
        else:
            state_action_returns.append((s,a,G))
        if r == None:
            r = 0
        G = r + GAMMA*G
        
    state_action_returns.reverse()
    g.reset()
    return state_action_returns
              

def monte_carlo():
    policy = {}
    Q = {}
    returns = {}
    for episode in tqdm(range(EPISODES)):
        action_state_returns = play_episode(policy , Q , returns)
        for s , a , G in action_state_returns:
            sa = (s , a)
            returns[sa].append(G)
            Q[s][a] = np.mean(returns[sa])
        
        #improve policy
        for s in policy:
            max_k = None
            max_v = float('-inf')
            for k ,v in Q[s].items():
                if max_v < v:
                    max_v = v
                    max_k = k
            policy[s] = max_k
    return policy


def test(policy):
    g.reset()
    while(True):
        a = get_epsilon_action(policy.get( g.get_state() , np.random.choice(g.get_possible_actions()) ) , EPISILON)
        r = g.perform_move(a , 'X')
        g.print_board()
       
        if r > 0:
            print('B')
            time.sleep(1)
            g.reset()
            g.print_board()
            continue
        x = int(input("move : "))
        r = g.perform_move(x , 'O')
        g.print_board()
        time.sleep(1)
        if r > 0:
            print('P')
            g.reset()
            g.print_board()


if __name__ == "__main__":
    policy = monte_carlo()
    test(policy)
   
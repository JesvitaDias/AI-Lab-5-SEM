import random
import math
def heuristic(state):
    h = 0
    n=len(state)
    for i in range(n):
        for j in range(i+1,n):
            if state[i]==state[j]:
                h+=1
            if abs(state[i]-state[j])==abs(i-j):
                h+=1
    return h
def generaterandomstate(n):
    return [random.randint(0,n-1) for _ in range(n)]
def randomneighbor(state):
    n=len(state)
    neighbor=state.copy()
    c=random.randint(0,n-1)
    r=random.randint(0,n-1)
    while r==neighbor[c]:
        r=random.randint(0,n-1)
    neighbor[c]=r
    return neighbor
def simulatedannealing(n,T,coolingrate):
    current=generaterandomstate(n)
    print("start state:",current,"h=",heuristic(current))
    while T>0:
        currenth=heuristic(current)
        if currenth==0:
            print("reached goal state:",current,"h=",currenth)
            return current
        neighbor=randomneighbor(current)
        neighborh=heuristic(neighbor)
        delta=neighborh-currenth
        if delta<0:
            current=neighbor
        else:
            P=math.exp(-delta/T)
            if random.random()<P:
                current=neighbor
        print("next state chosen:",current,"h=",heuristic(current))
        T*=coolingrate
    print("final state:",current,"h=",heuristic(current))
    return current
n=int(input("enter number of queens:  "))
T=100.0
coolingrate=0.99
solution=simulatedannealing(n, T, coolingrate)

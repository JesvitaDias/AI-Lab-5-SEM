import random
def heuristic(state):
    h=0
    n=len(state)
    for i in range(n):
        for j in range(i+1,n):
            if state[i]==state[j]:
                h+=1
            if abs(state[i]-state[j])==abs(i-j):
                h+=1
    return h
def hillclimbing(state):
    print("Start state:", state, "h =", heuristic(state))
    while True:
        currenth=heuristic(state)
        if currenth==0:
            print("Reached goal state:", state, "h =", currenth)
            return state
        neighbors=[]
        n=len(state)
        for c in range(n):
            for r in range(n):
                if r!=state[c]:
                    newstate=state.copy()
                    newstate[c]=r
                    neighbors.append(newstate)
        bestneighbor=min(neighbors, key=heuristic)
        besth=heuristic(bestneighbor)
        print("Next state chosen:", bestneighbor, "h =", besth)
        if besth>=currenth:
            print("Stuck at local minimum:", state, "h =", currenth)
            return state
        state=bestneighbor
n=int(input("Enter number of queens: "))
startstate=[random.randint(0, n-1) for _ in range(n)]
solution=hillclimbing(startstate)

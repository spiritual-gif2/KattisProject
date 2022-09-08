import copy
try:
    playersList = []
    n = int(input())

    for i in range(n):
        playersList.append(input())
    
    increase = copy.copy(playersList)
    increase.sort()
    decrease = copy.copy(playersList)
    decrease.sort(reverse = True)

    if playersList == increase:print("INCREASING")
    elif playersList == decrease:print("DECREASING")
    else:print("NEITHER")
    

except:''
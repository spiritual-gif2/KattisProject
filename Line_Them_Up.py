import copy

try:
    n = int(input())

    playersList = [input() for _ in range(n)]
    increase = copy.copy(playersList)
    increase.sort()
    decrease = copy.copy(playersList)
    decrease.sort(reverse=True)

    if playersList == increase:
        print("INCREASING")
    elif playersList == decrease:
        print("DECREASING")
    else:
        print("NEITHER")


except Exception:
    ''

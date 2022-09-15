freeFoodDays = []
try:
    N = int(input())
    if N in range(1, 101):
        for i in range(N):
            s, t = [int(x) for x in input().split()]
            eventDay = list(range(s, t + 1))
            for j in eventDay:
                if j not in freeFoodDays:
                    freeFoodDays.append(j)
        print(len(freeFoodDays))
except:
    ''

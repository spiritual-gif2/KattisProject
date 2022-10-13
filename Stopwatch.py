chronoRecord = []
chronoDisplay = 0
N = int(input())
if N%2 == 1:
    print("still running")
    pass
else:
    for i in range(N):
        chronoRecord.append(int(input()))
    for i in range(0,N,2):
        chronoDisplay += chronoRecord[i+1]-chronoRecord[i]
    print(chronoDisplay)
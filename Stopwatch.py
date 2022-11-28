chronoRecord = []
chronoDisplay = 0
N = int(input())
if N % 2 == 1:
    print("still running")
else:
    chronoRecord.extend(int(input()) for _ in range(N))
    for i in range(0, N, 2):
        chronoDisplay += chronoRecord[i + 1] - chronoRecord[i]
    print(chronoDisplay)

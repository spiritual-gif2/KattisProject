X = int(input())
N = int(input())
C = 0
for _ in range(N):
    C = C + X - int(input())
print(C + X)

W = int(input())
N = int(input())
totalArea = 0
for i in range(N):
    width, lenght = [int(j) for j in input().split()]
    totalArea += width * lenght
print(totalArea // W)

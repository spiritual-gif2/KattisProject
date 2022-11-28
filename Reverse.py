n = int(input())
numberList = [int(input()) for _ in range(n)]
for i in range(1, n + 1):
    print(numberList[-i])

numberList = []
n = int(input())
for i in range(n):
    numberList.append(int(input()))
for i in range(1,n+1):
    print(numberList[-i])
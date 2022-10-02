dataList = []
dataSet = int(input())

for i in range(dataSet):
    [num, days] = [int(i) for i in input().split()]
    days = sum(list(range(1, days + 1))) + days
    dataList.append([num, days])

for i in dataList:
    print(i[0], i[1])

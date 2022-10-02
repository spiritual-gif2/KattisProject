recordsNum = int(input())
recordsData = [int(i) for i in input().split() if int(i) < 0]
coldDays = len(recordsData)
print(coldDays)
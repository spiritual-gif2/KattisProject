n, Dm = [int(x) for x in input().split()]
pastRecords = [int(x) for x in input().split()]
if len(pastRecords) == n:
    index = -1
    for i in pastRecords:
        if i <= Dm:
            index = pastRecords.index(i)
    if index != -1:
        print(f"It had’t snowed this early in {index} years!")
    else:
        print("It had never snowed this early!")

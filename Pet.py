nightsRecords = []
for _ in range(5):
    oneNightRecord = [int(i) for i in input().split()]
    nightsRecords.append(sum(oneNightRecord))

winner = max(nightsRecords)
print(nightsRecords.index(winner) + 1, winner)

currentRating = 0

n,k = [int(i) for i in input().split()]

for j in range(k):
    currentRating += int(input())

minRating = (currentRating - (3*(n-k)))/n
maxRating = (currentRating + (3*(n-k)))/n

print(minRating,maxRating)
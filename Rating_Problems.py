n,k = [int(i) for i in input().split()]

currentRating = sum(int(input()) for _ in range(k))
minRating = (currentRating - (3*(n-k)))/n
maxRating = (currentRating + (3*(n-k)))/n

print(minRating,maxRating)
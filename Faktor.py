articles, impact = [int(i) for i in input().split()]
scientist = (articles * (impact - 1)) + 1
print(scientist)

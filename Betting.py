switchRatio = int(input())
poundA = 100 / switchRatio
poundB = 100 / (100 - switchRatio)
print(poundA.__round__(10))
print(poundB.__round__(10))

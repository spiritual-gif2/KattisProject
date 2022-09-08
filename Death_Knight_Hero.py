listOfBattle = []
numberOfWin = 0
n = int(input())
# Battles records
for i in range(n):
    listOfBattle.append(input())

for i in listOfBattle:
    currentBattle = list(i)
    win = True
    for i in range(len(currentBattle)-1):
        if currentBattle[i] == "C" and currentBattle[i + 1] == "D":
            win = False
            break
    if win:
        numberOfWin += 1
print(numberOfWin)
words = int(input())
wordsList = []
for i in range(words):
    wordsList.append(input())

for i in range(words):
    if (i+1) % 2 == 1:
        print(wordsList[i])

words = int(input())
wordsList = [input() for _ in range(words)]
for i in range(words):
    if (i+1) % 2 == 1:
        print(wordsList[i])

letters = "ABC"
dic = {}

inputList = list(int(x) for x in input().split())
inputLetters = input()

inputList.sort()
for i in range(len(letters)):
    dic[letters[i]] = inputList[i]

outputList = []
for i in range(len(inputLetters)):
    outputList.append(dic[inputLetters[i]])

reach = ''
for i in outputList:
    reach += str(i)
    reach += " "
print(reach)
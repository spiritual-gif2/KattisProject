def leave(ilist, lname):
    del ilist[ilist.index(lname)]


def cut(ilist, fName, lName):
    lNamePosition = ilist.index(lName)
    ilist.insert(lNamePosition, fName)


try:
    nameList = []
    N = int(input())
    for i in range(N):
        nameList.append(input())

    C = int(input())
    for i in range(C):
        inputCommand = input().split()

        if len(inputCommand) == 2:
            a, b = inputCommand
            if b in nameList:
                leave(nameList, b)

        elif len(inputCommand) == 3:
            a, b, c = inputCommand
            if c in nameList:
                cut(nameList, b, c)

    for name in nameList:
        print(name)
except:
    ''

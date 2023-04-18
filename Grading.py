grades = [int(i) for i in input().split()]
gradesLetters = list("ABCDEF")
mark = int(input())
find = False

for i in grades:
    if mark >= i:
        print(gradesLetters[grades.index(i)])
        find = True
        break
if not find:
    print(gradesLetters[-1])

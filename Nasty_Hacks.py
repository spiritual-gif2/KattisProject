answer = []
try:
    n = int(input())
    if n in range(1, 101):
        for i in range(n):
            r, e, c = [int(x) for x in input().split()]
            if (
                    r in range(-1000000, 1000001) and
                    e in range(-1000000, 1000001) and
                    c in range(0, 1000001)
            ):
                dif = e - c
                if dif > r:
                    answer.append("advertise")
                elif dif == r:
                    answer.append("does not matter")
                else:
                    answer.append("do not advertise")
        for i in answer:
            print(i)

except:
    ''

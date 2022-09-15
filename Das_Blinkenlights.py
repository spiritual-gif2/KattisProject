p, q, s = [int(x) for x in input().split()]
listP = [p * i for i in range(1, 10001) if p * i <= s]
listQ = [q * i for i in range(1, 10001) if q * i <= s]
blink = False

for i in listP:
    if i in listQ:
        print("yes")
        blink = True
        break

if not blink:
    print("no")

i = 0
out = 0
next = True
try:
    i = int(input())
    if i in range(1,101):
        for a in range(i):
            q,y = input().split()
            y = float(y)
            q = float(q)
            out += y*q
        if next:
            print(f"{out:.3f}")
except:
    ''
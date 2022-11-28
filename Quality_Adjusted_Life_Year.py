i = 0
out = 0
try:
    i = int(input())
    if i in range(1, 101):
        for _ in range(i):
            q, y = input().split()
            y = float(y)
            q = float(q)
            out += y * q
        print(f"{out:.3f}")
except:
    ''

try:
    n = int(input())
    hailstoneSeq = []

    while n >= 1:
        hailstoneSeq.append(n)
        if n == 1:
            break
        elif n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    print(len(hailstoneSeq))
except Exception:
    ''

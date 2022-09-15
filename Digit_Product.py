def prod(liste):
    pro = 1
    for i in liste:
        pro *= i
    return pro


def left(liste, y):
    while y in liste:
        liste.remove(y)


try:
    x = input()
    x = int(x)
    while x >= 10:
        x = str(x)
        x = [int(i) for i in x]
        left(x, 0)
        x = prod(x)
    print(x)
except:
    ''

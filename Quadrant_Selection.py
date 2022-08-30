try:
    x = int(input())
    y = int(input())
    if x != 0 and y != 0:
        if x > 0:
            if y > 0:
                print(1)
                pass
            else:
                print(4)
                pass
        else:
            if y > 0:
                print(2)
                pass
            else:
                print(3)
                pass
except:
    ''
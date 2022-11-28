# QUADRANT SELECTION FROM OpenKattis

try:
    # CONVERSION OF THE INPUT INTO AN INTEGER
    x = int(input())
    y = int(input())

    # INSURANCE THAT BOTH x AND y ARE HIGHER THAN 0
    if x != 0 and y != 0:
        # x AND y POSITION CONTROL
        if x > 0:
            if y > 0:
                print(1)
            else:
                print(4)
        elif y > 0:
            print(2)
        else:
            print(3)
except:
    ''

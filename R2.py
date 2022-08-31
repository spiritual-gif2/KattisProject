try:
    R1,S = input().split()
    R1 = int(R1)
    S = int(S)
    if (R1 in range(-1000,1001)) and (S in range(-1000,1001)):
        R2 = 2*S - R1
        print(R2)
except:
    ''
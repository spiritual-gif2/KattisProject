output = 0
try:
    N = int(input())
    if N in range(1, 11):
        for _ in range(N):
            uInput = int(input())
            number, power = divmod(uInput, 10)
            output += pow(number, power)
        print(output)
except:
    ''

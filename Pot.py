output = 0
try:
    N = int(input())
    if N in range(1,11):
        for i in range(N):
            uInput = int(input())
            number = uInput//10
            power = uInput%10
            output += pow(number,power)
        print(output)
except:
    ''
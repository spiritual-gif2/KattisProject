
try:
    #Return True if x+y == z and return False if not
    def addition(x,y,z):
        return (x+y == z)

    #Return True if x-y == z and return False if not
    def subtraction(x,y,z):
        return (x-y == z)

    #Return True if x*y == z and return False if not
    def multiplication(x,y,z):
        return (x*y == z)

    #Return True if x//y == z and return False if not
    def division(x,y,z):
        return (x/y == z)

    ans = []
    N = int(input())
    for i in range(N):
        a,b,c = [int(x) for x in input().split()]
        if ((a in range(1,10001)) and (b in range(1,10001)) and (c in range(1,10001))):
            condition1 = addition(a,b,c) or addition(b,a,c)
            condition2 = subtraction(a,b,c) or subtraction(b,a,c)
            condition3 = multiplication(a,b,c) or multiplication(b,a,c)
            condition4 = division(a,b,c) or division(b,a,c)
            if condition1 or condition2 or condition3 or condition4:
                ans.append("Possible")
            else:ans.append("Impossible")
    for i in ans:
        print(i)
except:
    ''


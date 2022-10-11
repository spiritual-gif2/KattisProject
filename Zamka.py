"""
    Function to add all the digits in a giving number
"""


def getSum(n: str):
    digitSum = 0
    for digit in n:
        digitSum += int(digit)
    return digitSum


"""
    Program start
"""
L = int(input())
D = int(input())
X = int(input())

numbersList = sorted([i for i in range(L, D+1) if getSum(str(i)) == X])
print(numbersList[0])
print(numbersList[len(numbersList) - 1])

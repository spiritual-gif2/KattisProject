def gcd(a_: int, b_: int) -> int:
    if b_ > a_:
        a_, b_ = b_, a_
    return a_ if b_ == 0 else gcd(b_, a_ % b_)


a, b = [int(i) for i in input().split()]
print(gcd(a, b))

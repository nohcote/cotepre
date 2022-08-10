import math


def is_prime(n):
    if n <= 1: return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True


M = int(input())
N = int(input())
arr = range(M, N+1)
primearr = []
for a in arr:
    if is_prime(a):
        primearr.append(a)
if len(primearr) > 0:
    print(sum(primearr), min(primearr))
else:
    print(-1)

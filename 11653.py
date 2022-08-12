import math


def getprimes(num):
    if num == 1:
        return []
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return getprimes(i) + getprimes(int(num/i))
    return [num]

[print(p) for p in getprimes(int(input()))]
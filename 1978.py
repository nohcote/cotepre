import math


def is_prime(n):
    if n <= 1: return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True


input()
arr = list(map(int, input().split()))
count = 0
for a in arr:
    if is_prime(a):
        count += 1
print(count)

import math
import sys


def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


arr = []
for a in range(2, 123456*2+1):
    if is_prime(a):
        arr.append(a)
while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    print(len(set(arr) & set(range(num+1, num*2+1))))
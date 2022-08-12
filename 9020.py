import sys


def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


for T in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())    
    for i in range(num//2, num-1):
        if is_prime(num-i) and is_prime(i):
            print(num-i, i)
            break
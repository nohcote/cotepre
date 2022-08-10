import math


for i in range(int(input())):
    k = int(input())
    n = int(input())
    print(math.comb(k+n, n-1))
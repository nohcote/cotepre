import sys
from math import gcd, lcm


A, B = map(int, sys.stdin.readline().split())
print(gcd(A, B))
print(lcm(A, B))
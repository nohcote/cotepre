import sys
from math import lcm


for T in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    print(lcm(A, B))
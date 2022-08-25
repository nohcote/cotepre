import sys
from itertools import permutations


a, b = map(int, sys.stdin.readline().split())
for e1 in permutations(range(1, a+1), b):
    [print(e2, end=" ") for e2 in e1]
    print()
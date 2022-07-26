import math
import sys


inp = int(sys.stdin.readline())

for _ in range(inp):
    n, m = map(int, sys.stdin.readline().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)

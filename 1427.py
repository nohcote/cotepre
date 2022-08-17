import sys


arr = sorted(list(map(int, [s for s in str(sys.stdin.readline().rstrip())])), reverse=True)
[print(a, end='') for a in arr]
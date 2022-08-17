import sys


N = int(input())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())
[print(a) for a in sorted(set(arr), key=lambda x:(len(x), x))]
import sys


N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)
[print(e) for e in arr]
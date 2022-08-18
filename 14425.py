import sys


N, M = map(int, sys.stdin.readline().split())
S = set(sys.stdin.readline().rstrip() for _ in range(N))
arrM = list(sys.stdin.readline().rstrip() for _ in range(M))

count = 0
for e in arrM:
    if e in S:
        count += 1
print(count)
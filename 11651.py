import sys


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
[print(f"{a[0]} {a[1]}") for a in sorted(arr, key=lambda x:(x[1], x[0]))]
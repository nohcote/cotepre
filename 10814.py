import sys


N = int(input())
arr = []
for _ in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    arr.append([int(age), name])
[print(f"{x[0]} {x[1]}") for x in sorted(arr, key=lambda x: x[0])]
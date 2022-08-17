import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
darr = {}
count = 0
for e in sorted(set(arr)):
    darr[e] = count
    count += 1
[print(e, end=" ") for e in [darr[x] for x in arr]]
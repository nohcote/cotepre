import sys


N = int(sys.stdin.readline())
arr = {}
for _ in range(N):
    temp = int(sys.stdin.readline())
    if temp in arr:
        arr[temp] += 1
    else:
        arr[temp] = 1
for a in sorted(arr.items()):
    for b in range(0, a[1]):
        print(a[0])
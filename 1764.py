import sys


N, M = list(map(int, sys.stdin.readline().split()))

arr1 = {sys.stdin.readline().rstrip() for _ in range(N)}
arr2 = {sys.stdin.readline().rstrip() for _ in range(M)}
arr3 = sorted(arr1 & arr2)
print(len(arr3))
for e in arr3:
    print(e)
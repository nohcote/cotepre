from collections import Counter
import sys


N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))
arr1_c = Counter(arr1)
for e in arr2:
    print(arr1_c[e], end=" ")
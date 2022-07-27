import sys


arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = [x**2 for x in arr]
print(sum(arr)%10)
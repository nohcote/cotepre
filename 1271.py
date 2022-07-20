import sys


n, m = list(map(int, sys.stdin.readline().rstrip().split()))

print(n//m)
print(int(n%m))
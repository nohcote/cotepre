import sys


N, k = map(int, sys.stdin.readline().rstrip().split())
print(sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)[k-1])
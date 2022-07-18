import sys


n, x = list(map(int, sys.stdin.readline().rstrip().split()))
temp = sys.stdin.readline().rstrip().split()
for i in range(0, len(temp)):
    if int(temp[i]) < x:
        print(temp[i], end=' ')
import sys


n = int(sys.stdin.readline().rstrip())
for i in range(0, n):
    a = sys.stdin.readline().rstrip()
    print(a[0]+a[-1])
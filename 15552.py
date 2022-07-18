import sys


testcase = int(sys.stdin.readline().rstrip())
for i in range(0, testcase):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    print(a+b)
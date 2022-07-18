import sys


n = int(sys.stdin.readline().rstrip())
arr = sys.stdin.readline().rstrip().split()
v = int(sys.stdin.readline().rstrip())

print(arr.count(str(v)))
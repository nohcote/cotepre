import sys


N = int(sys.stdin.readline())
arr1 = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

tempstr = ""
for e in arr2:
    if e in arr1:
        tempstr += "1 "
    else:
        tempstr += "0 "
print(tempstr)
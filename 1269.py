import sys


sys.stdin.readline()

arr1 = set(sys.stdin.readline().split())
arr2 = set(sys.stdin.readline().split())
arr3 = arr1 ^ arr2
print(len(arr3))
import sys


x, y, w, h = list(map(int, sys.stdin.readline().rstrip().split()))

x = w - x if x > w - x else x
y = h - y if y > h - y else y
print(x if x < y else y)
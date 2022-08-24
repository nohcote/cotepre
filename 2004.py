import sys


def getcount(x, y):
    count = 0
    while y <= x:
        x //= y
        count += x
    return count


n, m = map(int, sys.stdin.readline().split())

x1, y1 = getcount(n, 2), getcount(n, 5)
x2, y2 = getcount(n-m, 2), getcount(n-m, 5)
x3, y3 = getcount(m, 2), getcount(m, 5)

print(min(x1-x2-x3, y1-y2-y3))
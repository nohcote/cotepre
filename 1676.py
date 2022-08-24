import sys


def getcount(x, y):
    count = 0
    while y <= x:
        x //= y
        count += x
    return count


N = int(sys.stdin.readline())
x, y = getcount(N, 2), getcount(N, 5)

print(min(x, y))
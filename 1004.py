import sys


for i in range(int(sys.stdin.readline())):
    result = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(int(sys.stdin.readline())):
        cx, cy, r = map(int, sys.stdin.readline().split())
        d1 = (((x1-cx) ** 2) + ((y1-cy) ** 2)) ** 0.5
        d2 = (((x2-cx) ** 2) + ((y2-cy) ** 2)) ** 0.5
        if (d1<r and d2>r) or (d1>r and d2<r):
            result += 1
    print(result)

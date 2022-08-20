import sys


# (a,b), (c,b), (a,d), (c,d)
x = {}
y = {}
x1, y1 = tuple(map(int, sys.stdin.readline().split()))
x[x1] = x.get(x1, 0) + 1
y[y1] = y.get(y1, 0) + 1
x2, y2 = tuple(map(int, sys.stdin.readline().split()))
x[x2] = x.get(x2, 0) + 1
y[y2] = y.get(y2, 0) + 1
x3, y3 = tuple(map(int, sys.stdin.readline().split()))
x[x3] = x.get(x3, 0) + 1
y[y3] = y.get(y3, 0) + 1

for k1, v1 in x.items():
    if v1 == 1:
        print(k1, end=" ")
for k2, v2 in y.items():
    if v2 == 1:
        print(k2, end=" ")

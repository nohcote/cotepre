import sys


w, h, x, y, p = map(int, sys.stdin.readline().split())
result = 0
for i in range(p):
    r = h/2
    px, py = map(int, sys.stdin.readline().split())
    d1 = ((px-x)**2 + (py-y-r)**2)**0.5
    d2 = ((px-x-w)**2 + (py-y-r)**2)**0.5
    if (x<=px<=x+w and y<=py<=y+h) or d1<=r or d2<=r:
        result += 1
print(result)

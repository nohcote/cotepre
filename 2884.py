import sys


hour, min = map(int, sys.stdin.readline().rstrip().split())
if min - 45 >= 0:
    min = min - 45
elif hour - 1 >= 0:
    min = 15 + min
    hour -= 1
else:
    min = 15 + min
    hour = 23
print(hour, min)
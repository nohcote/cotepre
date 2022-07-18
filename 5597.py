import sys


arr = []
for x in range(0, 28):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)

for i in range(1, 30+1):
    if i not in arr:
        print(i)
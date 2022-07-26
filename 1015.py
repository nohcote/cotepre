import sys


length = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = a.copy()
b.sort()
dupdict = {}

for i in range(len(b)):
    if b[i] in a:
        if a[i] in dupdict:
            dupdict[a[i]] += 1
        else:
            dupdict[a[i]] = 0
        print(b.index(a[i])+dupdict[a[i]], end=' ')

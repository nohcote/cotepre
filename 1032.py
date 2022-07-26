import sys


n = int(sys.stdin.readline())
a = list(sys.stdin.readline())
for i in range(n-1):
    b = list(sys.stdin.readline())
    for j in range(len(a)):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))
import sys


n = int(sys.stdin.readline())
a = list(sys.stdin.readline())
a_len = len(a)
for i in range(n - 1):
    b = list(sys.stdin.readline())
    for j in range(a_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))
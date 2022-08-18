import sys


s = sys.stdin.readline().rstrip()
arr = []
for i in range(len(s)+1):
    for j in range(i+1, len(s)+1):
        arr += [s[i:j]]
print(len(set(arr)))
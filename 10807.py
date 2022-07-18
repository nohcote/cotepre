import sys


n = int(sys.stdin.readline().rstrip())
arr = sys.stdin.readline().rstrip().split()
v = int(sys.stdin.readline().rstrip())

count = 0

for i in range(0, len(arr)):
    if int(arr[i]) == v:
        count += 1
        
print(count)
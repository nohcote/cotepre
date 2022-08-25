import sys
from collections import Counter, deque


tc = int(sys.stdin.readline())
for i in range(tc):
    n = int(sys.stdin.readline())
    kind = deque()
    
    for j in range(n):
        a, b = sys.stdin.readline().rstrip().split()
        kind.append(b)
        
    kindcnt = 1    
    for index, value in Counter(kind).items():
        kindcnt *= value+1
        
    print(kindcnt-1)
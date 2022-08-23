import sys
import math
from collections import deque


N = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(N)])

newarr = deque()
for i in range(1, N):
    newarr.append(arr[i] - arr[i-1])

val_gcd = newarr.popleft()
for j in range(len(newarr)):
    val_gcd = math.gcd(val_gcd, newarr[j])

compareset = set()
for M in range(2, int(val_gcd**0.5)+1):
    if val_gcd % M == 0:
        compareset.add(M)
        compareset.add(val_gcd//M)

compareset.add(val_gcd)
print(*sorted(compareset))
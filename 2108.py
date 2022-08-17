from collections import Counter
import sys


N = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(N)])
print(round(sum(arr)/N))
print(arr[N//2])
mostarr = Counter(arr).most_common()
if N==1:
    print(arr[0])
elif mostarr[0][1] != mostarr[1][1]:
    print(mostarr[0][0])
else:
    print(mostarr[1][0])
print(arr[N-1]-arr[0])
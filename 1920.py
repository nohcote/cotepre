import sys


input = sys.stdin.readline
N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

result = ["1" if e in A else "0" for e in B]
print("\n".join(result))

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
[print(e) for e in arr]
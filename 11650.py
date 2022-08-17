N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
[print(f"{a[0]} {a[1]}") for a in sorted(arr)]
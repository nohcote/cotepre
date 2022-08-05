num = 2
arr = set(range(1, 10001))

for i in range(1, 10001):
    arr = set(arr) - set([i + sum([int(x) for x in str(i)])])
arr = list(arr)
arr.sort()
[print(a) for a in arr]
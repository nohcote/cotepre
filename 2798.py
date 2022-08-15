N, M = map(int, input().split())
l = list(map(int, input().split()))

val = 0
for i in range(len(l)):
    for j in range(i+1, len(l)):
        for k in range(j+1, len(l)):
            if l[i]+l[j]+l[k] <= M and l[i]+l[j]+l[k] > val:
                val = l[i] + l[j] + l[k]

print(val)
total = int(input())
num = int(input())
tocompare = 0
for i in range(num):
    temp = list(map(int, input().split()))
    tocompare += int(temp[0]*temp[1])
print("Yes" if total == tocompare else "No")
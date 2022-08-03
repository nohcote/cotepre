from collections import Counter

a = int(input())
b = int(input())
c = int(input())
temp = a*b*c
[print(str(temp).count(str(i))) for i in range(10)]
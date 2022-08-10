import math


a, b, v = map(int, input().split())
count = 1
# x = v-a / (a-b) + 1
print(int(1+math.ceil((v-a)/(a-b))))

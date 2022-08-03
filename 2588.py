import sys


a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

for i in range(len(list(b))):
    print(int(a) * int(b[-i-1]))
print(int(a)*int(b))
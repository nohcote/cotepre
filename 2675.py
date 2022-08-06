num = input()
for i in range(int(num)):
    length, s = input().split()
    [print("".join(x*int(length)), end="") for x in s]
    print()
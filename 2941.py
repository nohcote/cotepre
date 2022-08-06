arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
temp = input()
for a in arr:
    temp = temp.replace(a, " ")
print(len(temp))

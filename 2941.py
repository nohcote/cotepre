arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

temp = input()
total = 0
for a in arr:
    total += temp.count(a)
    temp = temp.replace(a, " ")
temp = temp.replace(" ", "")
print(total+len(temp))
x = int(input())
y = int(input())
if x > 0 and y > 0: # +, +
    result = 1
elif x > 0 and y < 0: # +, -
    result = 4
elif x < 0 and y < 0: # -, -
    result = 3
else: # -, +
    result = 2
print(result)
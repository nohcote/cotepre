inp = input().split(' ')
if int(inp[0]) > int(inp[1]):
    inp = '>'
elif int(inp[0]) < int(inp[1]):
    inp = '<'
else:
    inp = '=='
print(inp)

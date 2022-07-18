import sys


inp = sys.stdin.readline().rstrip()
for i in range(97, 122+1):
    print(inp.find(chr(i)), end=' ')
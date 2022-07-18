import sys


while True:
    n = sys.stdin.read(1)
    if not n.isalpha():
        break
    elif n.isupper():
        print(n.lower(), end='')
    elif n.islower():
        print(n.upper(), end='')
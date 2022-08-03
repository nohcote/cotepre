import sys


hour, min = map(int, sys.stdin.readline().rstrip().split())
newmin = int(sys.stdin.readline().rstrip())

hour += newmin // 60
newmin = newmin % 60

hour += (min + newmin) // 60
min = (min + newmin) % 60

while hour >= 24:
    hour -= 24
    
print(hour, min)
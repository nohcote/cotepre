import sys
from fractions import Fraction


int(sys.stdin.readline())
x, *arr = list(map(int, sys.stdin.readline().split()))
[print(f"{Fraction(x, e).numerator}/{Fraction(x, e).denominator}") for e in arr]
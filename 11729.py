def func(n, first, second, third):
    if n == 1:
        print(first, third)
    else:
        func(n-1, first, third, second)
        print(first, third)
        func(n-1, second, first, third)


num = int(input())
print(2**num - 1)
func(num, 1, 2, 3)
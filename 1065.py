N = int(input())

result = 0
for i in range(1, N+1):
    num_list = [int(x) for x in str(i)]
    if (i < 100) or (num_list[0]-num_list[1] == num_list[1]-num_list[2]):
        result += 1
print(result)
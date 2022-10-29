n = int(input())
num_list = list(map(int, input().split()))

sum = [num_list[0]]
for i in range(len(num_list)-1):
    sum.append(max(sum[i]+num_list[i+1], num_list[i+1]))
print(max(sum))


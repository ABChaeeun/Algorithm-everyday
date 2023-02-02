n = int(input())
lst = list(map(int, input().split()))

lst.sort()

sum = 0
for i in range(n):
    tmp = 0
    for j in range(i+1):
        tmp += lst[j]
    sum += tmp

print(sum)
n = int(input())
lst = list(map(int, input().split()))

sum = 0
sums = []
tmp = lst[0]
for i in range(n):
    if tmp > lst[i]: # tmp보다 낮은경우
        sum += 1
    elif tmp < lst[i]: # tmp보다 높은경우
        sums.append([tmp, sum])
        tmp = lst[i]
        sum = 0
sums.append([tmp, sum]) # 마지막꺼도 넣어주기!!

sums.sort(key = lambda x:(x[1], x[0]))
print(sums[-1][1])
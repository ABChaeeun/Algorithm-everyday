N = int(input())

cnt = 0
for i in range(N):
    num = i
    sum = i
    while num > 0:
        sum += num % 10
        num = num // 10
    if sum == N:
        print(i)
        cnt += 1
        break
        
if cnt == 0:
    print(0)
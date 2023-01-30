yen = int(input())
x = 1000 - yen
cnt = 0

lst = [500, 100, 50, 10, 5, 1]

for i in lst:
    cnt += x // i
    x %= i

print(cnt)
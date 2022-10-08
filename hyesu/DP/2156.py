import sys

input = sys.stdin.readline

n = int(input())
data = []
하
for _ in range(n):
    data.append(int(input()))

#  d[n] : n번째까지 마신 최대 잔
# d[n] = max(data[n] + d)

d = [0] * n

if n == 1:
    print(data[0])
elif n == 2:
    print(data[0] + data[1])
elif n == 3:
    print(max(data[1] + data[2], data[0] + data[1], data[0] + data[2]))
else:
    d[0] = data[0]
    d[1] = data[0] + data[1]
    d[2] = max(data[1] + data[2], data[0] + data[1], data[0] + data[2])

    for i in range(3, n):
        d[i] = max(d[i-1], d[i-2] + data[i], d[i-3] + data[i-1] + data[i])

    print(d[n-1])
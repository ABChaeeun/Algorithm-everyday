import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
d = [0] * (k+1)
d[0] = 1

for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for i in range(1, k+1):
        if i >= coin:
            d[i] += d[i-coin]

print(d[k])

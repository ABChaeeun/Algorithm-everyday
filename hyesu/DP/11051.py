import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [[1] * (k+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if j == 0:
            d[i][j] = 1
        elif j == i:
            d[i][j] = 1
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j]

print(d[n][k] % 10007)
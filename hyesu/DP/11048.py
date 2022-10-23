import sys
input = sys.stdin.readline

n, m = map(int, input().split())

candy = []
d = [[0] * m for _ in range(n)]

for i in range(n):
    candy.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            d[i][j] = candy[i][j]
        elif i == 0:
            d[i][j] = d[i][j-1] + candy[i][j]
        elif j == 0:
            d[i][j] = d[i-1][j] + candy[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i][j-1], d[i-1][j]) + candy[i][j]


print(d[n-1][m-1])
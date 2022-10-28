import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [[1] * n for _ in range(n)]


for i in range(1, n):
    for j in range(1, i):
        d[i][j] = d[i-1][j-1] + d[i-1][j]

print(d[n-1][k-1])


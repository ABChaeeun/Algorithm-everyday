# 쉬운 계단수

import sys
input = sys.stdin.readline

n = int(input())

d = [[1] * 10 for _ in range(n)]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][1]
        elif j == 9:
            d[i][j] = d[i-1][8]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]

print((sum(d[n-1]) - d[n-1][0]) %1000000000)

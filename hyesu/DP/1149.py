# RGB 거리

import sys
input = sys.stdin.readline

n = int(input())

d = [[0] * 3 for i in range(n)] #d[i] i번째 집까지 칠했을 때 최소 비용

# d[i][0] 지금색 r일때
# d[i][1] 지금색 g일때
# d[i][2] 지금색 b일때

cost = []

for _ in range(n):
    r, g, b = map(int, input().split())
    cost.append((r, g, b))

d[0][0] = cost[0][0]
d[0][1] = cost[0][1]
d[0][2] = cost[0][2]

for i in range(1, n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + cost[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + cost[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + cost[i][2]


print(min(d[n-1]))

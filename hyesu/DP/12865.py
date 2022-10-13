import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [(0, 0)]

for _ in range(n):
    w, v = map(int, input().split())
    data.append((w, v))

d = [[0]*(k+1) for _ in range(n+1)]

d[1][1] = data[1][1]

# 아이템을 하나씩 돌아가면서 체크한다.

for i in range(1, n+1):
    w = data[i][0]
    v = data[i][1]
    for j in range(1, k+1):
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j-w] + v, d[i-1][j])
print(d[n][k])
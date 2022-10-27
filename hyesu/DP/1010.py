import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    d = [[1] * m for _ in range(n)] 

    for i in range(n):
        for j in range(i, m):
            tmp = d[i-1][j: m]
            d[i][j] = sum(tmp)

    print(max(d[n-1]))
import sys
input = sys.stdin.readline

n = int(input())

d = [[1]*10 for _ in range(n)]

for i in range(1, n):
    for j in range(10):
        tmp = d[i-1][j:] # 1이면 1부터 10까지 슬라이스
        d[i][j] = sum(tmp)

print(sum(d[n-1])%10007)
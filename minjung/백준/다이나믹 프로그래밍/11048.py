import sys
input = sys.stdin.readline

n, m = map(int,input().split())
candy = []

for _ in range(n):(
    candy.append(list(map(int,input().split()))))

dp = [[0]*(m+1) for _ in range(n+1)] 
dp[0][0] = candy[0][0]

for i in range(n):
    for j in range(m):
        if i == 0:
            dp[i][j] = dp[i][j-1] +candy[i][j]
            continue
        if j == 0:
            dp[i][j] = dp[i-1][j]+ candy[i][j]
            continue
        dp[i][j] = max(dp[i-1][j]+candy[i][j],dp[i][j-1]+candy[i][j])

print(dp[n-1][m-1])
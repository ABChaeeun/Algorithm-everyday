import sys
input = sys.stdin.readline


n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0]*(n+1)
dp[0] = arr[0]
# dp[0] = arr[1]

if n >=2:
    dp[1] = arr[0]+arr[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+arr[i]+arr[i-1],dp[i-2]+arr[i])
        dp[i] = max(dp[i-1],dp[i])

print(dp[n-1])
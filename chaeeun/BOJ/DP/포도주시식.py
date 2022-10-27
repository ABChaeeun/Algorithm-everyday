# DP

n = int(input())

glass = [0] * 10001
for nn in range(1, n+1):
    glass[nn] = int(input())

dp = [0]*10001
dp[1] = glass[1]
dp[2] = glass[1] + glass[2]
for i in range(3, n+1): # 점화식 구현
    dp[i] = max(dp[i-1], dp[i-2]+glass[i], dp[i-3]+glass[i]+glass[i-1])


print(dp[n])
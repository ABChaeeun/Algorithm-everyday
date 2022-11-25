import sys
input = sys.stdin.readline

# 1 -> 0
# 2 -> 3
# 3 -> 0
# 4 -> dp[2]*dp[2]+2 = 11
#6 -> dp[4]*dp[2]+dp[2]*2+2 = 41
# 8 -> dp[6]*dp[2] +dp[4]*2 +dp[2]*2+2

n = int(input())
dp = [0]*31
dp[2] = 3

for i in range(4,n+1):
    if i%2 == 0:
        dp[i]+= dp[i-2]*dp[2]
        for j in range(i-4,-1,-2):
            dp[i]+=dp[j]*2
        dp[i]+=2

print(dp[n])
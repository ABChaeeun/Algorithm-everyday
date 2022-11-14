import sys
input = sys.stdin.readline


N = int(input())

schedule = []
dp = []

for _ in range(N):
    t, p = map(int,input().split())
    schedule.append((t,p))
    dp.append(p)
dp.append(0)

for i in range(N-1,-1,-1):
    if schedule[i][0] +i > N:
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1],schedule[i][1]+ dp[i+schedule[i][0]])

print(dp[0])
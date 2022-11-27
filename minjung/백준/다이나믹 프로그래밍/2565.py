import sys
input = sys.stdin.readline


n = int(input())
link = []

for _ in range(n):
    a,b = map(int,input().split())
    link.append([a,b])



delcount =0

# while True:
#     dp = [0]*len(link)
#     for ab in range(len(link)):
#         x1 ,y1 = link[ab][0],link[ab][1]
#         count = 0
#         for ab2 in link:
#             x2,y2 = ab2[0],ab2[1]
#             if x1<x2 and y1>y2:
#                 count+=1
#         dp[ab] = count
#     if max(dp) == 0:
#         break
#     idx = dp.index(max(dp))
#     del link[idx]
#     delcount+=1


# print(delcount)
    
link.sort(key = lambda x:x[0])
dp = [0]*n
for i in range(n):
    result_max = 0
    for j in range(i):
        if link[i][1]>link[j][1]:
            if result_max <dp[j]:
                  result_max = dp[j]
    dp[i] = result_max + 1

print(n-max(dp))
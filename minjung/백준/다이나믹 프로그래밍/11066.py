# 파일 합치기
# gold 3

# 계속 오류 난 이유 : 부분합을 배열로 넣ㄷ어줬는데 계산되는 부분에서 인덱스가 0일 때 -1로 들어가서 인덱스 값이 -1로 되어서 아이에 맨 뒤에값을 불러버려서 계속 마이너스 값으로 업뎃이 됐다 . .
# 백준은 pypy3로만 통과댐

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    novel = list(map(int,input().split()))
    # print(novel[0])
    dp = [[0]*n for _ in range(n)]
    subsum = [0 for _ in range(n)]
    subsum[0]= novel[0]

    sum= {-1:0}
    for i in range(n):
        sum[i] = sum[i-1]+ novel[i]
    

    for size in range(1,n):
        for start in range(n-1):
            end = start+size

            if end >= n:
                break
            
            result = int(1e9)
            
            for cut in range(start,end):
                result = min(result,dp[start][cut]+dp[cut+1][end]+(sum[end]-sum[start-1]))
            
            dp[start][end] = result

    print(dp[0][-1])
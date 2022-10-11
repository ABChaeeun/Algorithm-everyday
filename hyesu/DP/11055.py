# 가장 큰 증가 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

d = [0] * n 

d[0] = A[0]
# d[i] => i번째까지 했을때 합이 가장 큰 증가 부분수열의 합을 저장

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[j] + A[i], d[i])
        else:
            d[i] = max(d[i], A[i])

print(max(d))

# 파일 합치기
# gold 3

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    novel = list(map(int,input().split()))
    dp = [[0]*n for _ in range(n)]
    sum = []
    for i in range(n):
        sum[i] += novel[i]
    
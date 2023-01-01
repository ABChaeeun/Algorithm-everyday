# 팰린드롬?
# 골드 4

import sys
input = sys.stdin.readline


def dp_palin():
    for num_len in range(n):
        for start in range(n-num_len):
            end = start + num_len
            if start == end:    #시작점과 끝점이 같다면 글자수가 1개이므로 무조건 팰린드롬
                dp[start][end] = 1
            elif num[start] == num[end]:    #시작점의 글자와 끝점의 글자가 같다면
                if start + 1 == end :   #두 글자짜리 문자열이면 무조건 팰린드롬
                    dp[start][end]=1
                elif dp[start+1][end-1] == 1:   # 가운데 문자열이 팰린드롬이면 팰린드롬 
                    dp[start][end] = 1

n = int(input())
num = list(map(int,input().split()))
m = int(input())

dp = [[0]*n for _ in range(n)]

dp_palin()

for _ in range(m):
    s, e = map(int,input().split())
    print(dp[s-1][e-1])

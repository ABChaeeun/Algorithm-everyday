# 1. 2차원 배열을 사용한 동적 계획법

import sys
read = sys.stdin.readline

str1, str2 = read().strip(), read().strip()
n, m = len(str1), len(str2)
cache = [[0] * (m+1) for i in range(n+1)]

for j in range(1, n+1):
    for k in range(1, m+1):
        if str1[j-1] == str2[k-1]:
            cache[j][k] = cache[j-1][k-1] + 1
        else:
            cache[j][k] = max(cache[j-1][k], cache[j][k-1])

print(cache[-1][-1])
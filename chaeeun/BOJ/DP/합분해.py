# 참고

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

### 초기화
lst = []
for i in range(k):
    if i == 0:
        lst.append([1]*(n))
    else:
        lst.append([0]*(n))
    lst[i][0] = i+1

### 숫자 넣기
for i in range(1, k):
    for j in range(1, n):
        lst[i][j] = lst[i][j-1] + lst[i-1][j]

print(lst[-1][-1] % 1000000000)
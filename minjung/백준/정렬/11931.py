# 수 정렬하기 4
# ICPC 윈터 스터디

import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

num.sort(reverse=True)

for i in range(n) :
    print(num[i])
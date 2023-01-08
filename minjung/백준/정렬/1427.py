# 소트인사이드
# ICPC 윈터 스터디

import sys
input = sys.stdin.readline

n = list(str(input()))
num = []
for i in range(len(n)-1):
    num.append(int(n[i]))

num.sort(reverse=True)

for i in range(len(n)-1):
    print(num[i],end="")
# 국영수
# ICPC 윈터 스터디

import sys
input = sys.stdin.readline

n = int(input())
score = []
for _ in range(n):
    score.append(list(map(str,input().split())))

for i in range(n):
    score[i][1] = int(score[i][1])
    score[i][2] = int(score[i][2])
    score[i][3] = int(score[i][3])
score = sorted(score, key=lambda x:(-x[1],x[2],-x[3],x[0]))



for i in range(n):
    print(score[i][0])
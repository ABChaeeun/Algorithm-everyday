# 나이순 정렬
# ICPC 윈터 스터디

import sys
input = sys.stdin.readline

n = int(input())
user = []

for _ in range(n):
    age, name = map(str,input().split())

    user.append([int(age),name])

user = sorted(user, key=lambda x:x[0])

for i in range(n):
    print(user[i][0],user[i][1])
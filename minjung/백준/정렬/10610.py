# 30
# ICPC 윈터 스터디
import sys
input = sys.stdin.readline

n = list(str(input()))
num =[]
for i in range(len(n)-1):
    num.append(int(n[i]))

num.sort(reverse=True)

if sum(num)%3 == 0:
    if num[-1] == 0 :
        for j in range(len(num)):
            print(num[j],end='')
    else :
        print(-1)
else :
    print(-1)


# 참고 - set 이용

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

sett = sorted(list(set(lst)))

dictt = {}
for i in range(len(sett)):
    dictt[sett[i]] = i

for i in lst:
    print(dictt[i], end=' ')
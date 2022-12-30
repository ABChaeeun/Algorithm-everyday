# 설탕 배달
# 3과 5를 조합하여 담음
# if 문을 잘 활용하면 된다

import sys
input = sys.stdin.readline

n = int(input())

if n%5 == 0:
    print(n//5)
else :
    p = 0
    while n>0:
        n-=3
        p+=1
        if n%5 == 0:
            p += n//5
            print(p)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(p)
            break
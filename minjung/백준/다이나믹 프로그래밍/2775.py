import sys
input = sys.stdin.readline


def resident_num(k,n):
    for _ in range(k):
        for i in range(1,n):
            base[i] += base[i-1]
    return base[-1]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    base = [x for x in range(1,n+1)]
    print(resident_num(k,n))

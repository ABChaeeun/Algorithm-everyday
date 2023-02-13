# 참고

import sys
import heapq

n = int(input())
q = []

for i in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
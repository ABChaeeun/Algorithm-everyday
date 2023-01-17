# 참고(이해 후 내가 작성)

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split())) # queuestack
M = int(input())
C = list(map(int, input().split()))


deq = deque()
for i in range(N):
    if A[i] == 0:
        deq.append(B[i])
for k in range(M):
    # print(*deq)
    deq.appendleft(C[k])
    print(deq.pop(), end=' ')
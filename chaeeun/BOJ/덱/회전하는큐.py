# 참고

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
queue = deque([i for i in range(1, N + 1)]) # 1부터 시작해야!

cnt = 0
for i in lst:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) <= len(queue) / 2: # [참고 point] 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while queue[0] != i:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt += 1

print(cnt)
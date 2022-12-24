import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

visited = [0] * (N + 1)
lst = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lst[a][b] = 1
    lst[b][a] = 1


def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in range(1, N + 1):
            if (visited[i] == 0 and lst[v][i] == 1):
                visited[i] = 1  ### v가 아니라 i !!!
                queue.append(i)


answer = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        # print('i', i)
        bfs(i)
        answer += 1
print(answer)

# 참고..

import sys
from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        # print('queue ---------', *queue)
        x, y = queue.popleft()
        # print("i, j -", x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 1:
                queue.append((nx, ny))
                lst[nx][ny] = 2

    return 1


T = int(sys.stdin.readline())
for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # 가로, 세로

    lst = [[0]*M for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        lst[b][a] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                # print('\n\nlst[i][j]', i, j)
                answer += bfs(i, j)

    print(answer)

    # for i in range(N):
    #     print(*lst[i])

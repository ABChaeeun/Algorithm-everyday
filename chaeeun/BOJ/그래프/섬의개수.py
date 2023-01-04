from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]


def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    lst[i][j] = 2
    while queue:
        i, j = queue.popleft()
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if lst[nx][ny] == 1:
                    lst[nx][ny] = 2
                    queue.append([nx, ny])

M, N = 1, 1
while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    cnt = 0
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                bfs(i, j)
                cnt += 1
    # print(*lst)
    print(cnt)

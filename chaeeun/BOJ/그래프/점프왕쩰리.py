# 참고

from collections import deque

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

##### visited = [0]*N*N # visited도 똑같이 2차원 배열로 만들어주기!
visited = [[0] * N for _ in range(N)]
dx = [1, 0]  # 오른쪽으로만 이동
dy = [0, 1]  # 아래쪽으로만 이동


def bfs(x, y):

    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        step = lst[x][y]

        if (lst[x][y] == -1):
            return True

        for move in range(2):
            nx = x + dx[move] * step
            ny = y + dy[move] * step

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue  # 무시

            if (visited[nx][ny] == 0):
                visited[nx][ny] = 1
                queue.append([nx, ny])


if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")

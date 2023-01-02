import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, -1, -1, 1, 1, 1, 0, 0, 0]
dx = [0, -1, 1, 0, -1, 1, 0, -1, 1]

while True:
    w, h = map(int, input().split())
    if (w == 0) and (h == 0):
        break
    
    map_data = []
    visited = [[False] * w for _ in range(h)]
    queue = deque()
    for i in range(h):
        map_data.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if map_data[i][j] == 1:
                queue.append((j, i))
                while queue:
                    (a, b) = queue.popleft()
                    visited[b][a] = True
                    for k in range(9):
                        x = a + dx[k]
                        y = b + dy[k]
                        if x < 0 or x >= w or y < 0 or y >= h:
                            continue
                        else:
                            if map_data[y][x] == 1 and visited[y][x] == False:
                                queue.append((x, y))
                                map_data[y][x] = 0
    
    answer = 0
    for data in map_data:
        answer += sum(data)
    print(answer)

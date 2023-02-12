from collections import deque

def solution(maps):
    answer = False
    n = len(maps)
    m = len(maps[0])
    
    d = [[1] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
            if maps[new_x][new_y] == 1 and visited[new_x][new_y] == False:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                d[new_x][new_y] = d[x][y] + 1
            if new_x is n-1 and new_y is m-1:
                answer = True
                break
                
    if answer == False:
        return -1
    
    return d[n-1][m-1]
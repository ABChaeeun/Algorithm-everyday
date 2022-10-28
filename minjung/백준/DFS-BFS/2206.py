from collections import deque

queue = deque([])
def bfs(x,y,iscrash): 
    queue.append([x,y,iscrash])
    visited[x][y][iscrash] = 1
    d = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        x,y ,iscrash= queue.popleft()
        if x == N-1 and y == M-1 :
            return visited[x][y][iscrash]
        for dx, dy in d:
            nx , ny = x+dx, y+dy
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue
            if movemap[nx][ny] == 0 and visited[nx][ny][iscrash]==0:
                visited[nx][ny][iscrash] = visited[x][y][iscrash] + 1
                queue.append([nx,ny,iscrash])
            if movemap[nx][ny] == 1 and iscrash== 0 :
                visited[nx][ny][iscrash+1] = visited[x][y][iscrash] + 1
                queue.append([nx,ny,iscrash+1])
    return -1

N, M = map(int,input().split())

movemap = [list(map(int,input())) for _ in range(N)]



visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(bfs(0,0,0))

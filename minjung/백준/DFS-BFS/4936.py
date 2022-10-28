from collections import deque

def bfs(x,y):
    queue = deque([[x,y]])
    d = [(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,1),(1,-1),(-1,-1)]
    island[x][y] = 0
    cnt = 1
    while queue :
        x,y = queue.popleft()
        for dx,dy in d:
            nx, ny = x+dx,y+dy
            if (0 <=nx<h) and (0<=ny<w) and island[nx][ny] == 1:
                island[nx][ny] = 0
                queue.append([nx,ny])
                cnt+1
    return cnt
 

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0 :
        break
    island = [list(map(int,input().split())) for _ in range(h)]
    res = []
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                res.append(bfs(i,j))
    print(len(res))

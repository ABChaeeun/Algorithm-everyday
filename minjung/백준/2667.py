from collections import deque
import queue

def bfs(x,y):
    queue = deque([[x,y]])
    d = [(-1,0),(1,0),(0,-1),(0,1)]
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            mx,my = x+dx,y+dy
            if (0 <= mx <n) and (0<=my<n) and map_[mx][my]==1 and visited[mx][my]==0:
                visited[mx][my] = 1
                queue.append([mx,my])
                cnt+=1
    return cnt

n = int(input())

map_ = [list(map(int,input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
res =[]

for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and map_[i][j]== 1:
            visited[i][j]=1
            res.append(bfs(i,j))

print(len(res))
for i in range(len(res)):
    sort_res = sorted(res)
    print(sort_res[i])
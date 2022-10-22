from collections import deque

def bfs(x,y):
    queue = deque([[x,y]])
    d = [(-1,0),(1,0),(0,-1),(0,1)]
    bachu[x][y] = 0
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            nx , ny = x+dx,y+dy
            if (0<=nx<M) and (0<=ny<N) and bachu[nx][ny]==1:
                bachu[nx][ny] = 0
                queue.append([nx,ny])
                cnt += 1
    return cnt


T = int(input()) 

for _ in range(T):
    M, N, K = map(int,input().split())
    bachu = [[0]*N for _ in range(M)]
    for _ in range(K):
        x, y = map(int,input().split())
        bachu[x][y] = 1
    res = []
    for i in range(M):
        for j in range(N):
            if bachu[i][j] == 1:
                bachu[i][j] = 0
                res.append(bfs(i,j))
    print(len(res))


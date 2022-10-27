from collections import deque


def bfs(x,y):
    if miro[x][y] == 1:
        queue = deque([[x,y]])
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=ny<m and 0<=nx<n and  miro[nx][ny]==1:
                    miro[nx][ny] += miro[x][y]
                    queue.append([nx,ny])





n, m = map(int,(input().split()))
dx = [0,1,0,-1]
dy = [-1,0,1,0]

miro =[list(map(int,input())) for _ in range(n)]



bfs(0,0)
print(miro[n-1][m-1])

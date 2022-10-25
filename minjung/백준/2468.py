from collections import deque

def bfs(x,y,num):
    queue = deque([[x,y]])
    d = [(-1,0),(1,0),(0,1),(0,-1)]
    checkbfs[x][y] = 1
    cnt = 0
    while queue :
        x,y = queue.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if (0<=nx<n) and (0<=ny<n) and checkbfs[nx][ny] == 0 and distriction[nx][ny] > num:
                checkbfs[nx][ny] = 1
                queue.append([nx,ny])
                cnt+=1
    return cnt

def runbfs(k):
    cnt = 0
    res=[]
    for i in range(n):
        for j in range(n):
            if distriction[i][j]>k and checkbfs[i][j] == 0:
                res.append(bfs(i,j,k))
                cnt+=1
    return res


                
n = int(input())
distriction = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    maxnum=-1
    maxnum = max(maxnum,max(distriction[i]))

res = []
for k in range(maxnum):     
     checkbfs  = [[0]*n for _ in range(n)]
     kresult = runbfs(k)
     res.append(len(kresult))

print(max(res))

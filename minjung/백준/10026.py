#적록 색약
#dfs
import sys
sys.setrecursionlimit(10000) 



def dfs(y,x):
    visited[y][x] = 1
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if 0 <= ny <n and 0 <= nx <n:
            if depart[y][x] == depart[ny][nx] and not visited[ny][nx]:
                dfs(ny,nx)
            
def cw_dfs(y,x):
    cw_visited[y][x] = 1
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if 0 <= ny <n and 0 <= nx < n:
            cur = depart[y][x]
            if depart[y][x]==depart[ny][nx] and not cw_visited[ny][nx]:
                cw_dfs(ny,nx)
            elif depart[y][x] != depart[ny][nx] and not cw_visited[ny][nx]:
                if cur == 'G':
                    if depart[ny][nx] =='R':
                        cw_dfs(ny,nx)
                elif cur=='R':
                    if depart[ny][nx] == 'G' :
                        cw_dfs(ny,nx)
            

            
n= int(input())
depart = [list(map(str,input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cw_visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
cw_cnt = 0
dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt+=1

for i in range(n):
    for j in range(n):
        if not cw_visited[i][j]:
            cw_dfs(i,j)
            cw_cnt+=1

print(cnt,cw_cnt)
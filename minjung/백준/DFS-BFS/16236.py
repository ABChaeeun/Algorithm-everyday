from collections import deque


N = int(input())

sharkmap= [[0 for col in range(0,N)]for row in range(0,N)]

for i in range(0,N) :
    for j,k in enumerate(map(int,input().split())):
        sharkmap[i][j] = k


#아기상어 위치 확인 
nx,ny=-1,-1
level,eat = 2,0
for i in range(0,N):
    for j in range(0,N):
        if sharkmap[i][j] == 9 :
            sharkmap[i][j]=0
            nx=i
            ny=j
            break

dx=[-1,1,0,0]
dy=[0,0,-1,-1]

#bfs활용
def babyshark(nx,ny,level):
    visited = [[False]*N for _ in range(N)]
    q=deque()
    q.append((nx,ny,0))
  
    visited[nx][ny]=True
    fish=[]
    while q:
        x,y,count=q.popleft()
       
        for i in range(0,4):
            fx=x+dx[i]
            fy=y+dy[i]
            if 0 <= fx < N and 0 <= fy  <N and not visited[fx][fy]:
                visited[fx][fy] = True
                if sharkmap[fx][fy] != 0 and sharkmap[fx][fy] <level:
                    fish.append((count+1,fx,fy))
                    print(fish)
                    q.append((fx,fy,count+1))
                    
                elif sharkmap[fx][fy]==0 or sharkmap[fx][fy] == level :
                    q.append((fx,fy,count+1))
                
    fish.sort()
    if fish:
        return [fish[0][1],fish[0][2],fish[0][0]]
    else:
         return []

result=0
while True:
    shark_eat = babyshark(nx,ny,level)
   
    if shark_eat :
        x,y,move=shark_eat
        sharkmap[x][y]=0
        eat+=1
        result+=move
        print("shark eat")
        print(result)
        if eat == level :
            level+=1
            eat = 0  
        nx,ny = x,y
    else :
        break

print(result)
from collections import deque
N = int(input())

lst = []
for i in range(N):
    lst.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnts = []

def bfs(i, j):

    queue = deque()
    queue.append([i, j])
    
    lst[i][j] = 2

    cnt = 1
    while queue:
        i, j = queue.popleft()
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 1:
                lst[nx][ny] = 2
                queue.append([nx, ny])
                cnt += 1

    # print(cnt)
    cnts.append(cnt)

CNT = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            # print(i, j)
            bfs(i, j)
            CNT += 1
    
print(CNT)
cnts.sort()
for i in range(len(cnts)):
    print(cnts[i])

# for i in range(N):
#     print(*lst[i])




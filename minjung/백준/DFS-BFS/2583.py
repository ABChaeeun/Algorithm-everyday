from collections import deque


def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    d = [(-1,0),(1,0),(0,-1),(0,1)]
    cnt = 1
    while queue:
        y,x = queue.popleft()
        for dy,dx in d :
            Y,X = y+dy,x+dx
            if ( 0 <= Y < n ) and ( 0 <= X < m ) and box[Y][X]== 0:
                box[Y][X] = 1
                queue.append((Y,X))
                cnt += 1
    return cnt 


n , m , num  = map(int,input().split())

box = [[0]*m for _ in range(n)]
for _ in range(num):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            box[i][j] = 1

# for _ in range(num):
#     x1, y1, x2, y2 = map(int,input().split())
#     print('i',i,j)
#     for i in range(y1,y2):
#         for j in range(x1,x2):
#             box[i][j] = 1
#             print('i',i,j)

res = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            box[i][j] = 1
            res.append(bfs(i,j))

print(len(res))
print(*sorted(res))
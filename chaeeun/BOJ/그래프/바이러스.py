from collections import deque

computerNum = int(input())
nodeNum = int(input())

visit = [0]*(computerNum+1)
lst = [[0]*(computerNum+1) for _ in range(computerNum+1)]

for i in range(nodeNum):
    a, b = map(int, input().split())
    lst[a][b] = lst[b][a] = 1

# for i in range(computerNum+1):
#     print(*lst[i])

def bfs(v):
    global cnt
    visit[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft() ###
        # print(v, end=' ') ###
        cnt += 1
        for i in range(1, computerNum+1):
            if (visit[i] == 0 and lst[v][i] == 1):
                queue.append(i) ### v가 아니라 i
                visit[i] = 1
cnt = 0
bfs(1)
print(cnt - 1)

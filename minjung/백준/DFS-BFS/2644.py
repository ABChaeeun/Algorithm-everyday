from collections import deque

def bfs(start):
    queue  =deque([start])
    while queue:
        start = queue.popleft()
        for num in family[start]:
            if check[num] == 0:
                check[num] = check[start]+1
                queue.append(num)

n = int(input())
find_x,find_y = map(int,input().split())
m = int(input())

family = [[] for _ in range(n+1)]
for _ in range(m):
    x , y = map(int,input().split())
    family[x].append(y)
    family[y].append(x)

check = [0]*(n+1)
bfs(find_x)
print(check[find_y] if check[find_y]> 0 else '-1')

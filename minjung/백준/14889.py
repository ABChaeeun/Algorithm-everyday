from collections import deque




def dfs(depth,index):
    global min_diff
    if depth == n//2:#한 팀에 속한 팀원의 명수가 n//2로 다 채워졌면 능력치를 비교
        stark ,link = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]: #stak가 방문
                    stark += stark_link[i][j]
                elif not visited[i] and not visited[j]:#stark팀을 제외하고 팀을 구성해야 함
                    link += stark_link[i][j]
        min_diff = min(min_diff, abs(stark-link))
         
    
    for i in range(index,n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i+1)
            visited[i] = False

n = int(input())

stark_link = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
min_diff = int(1e9)
dfs(0,0)
print(min_diff)

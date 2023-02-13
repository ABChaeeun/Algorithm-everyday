from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [False] * n
    
    for i in range(n):
        print(visited)
        if visited[i] == False:
            answer += 1
            queue.append(i)
            visited[i] = True
            
            while queue:
                v = queue.popleft()
                for j in range(n):
                    if computers[v][j] == 1 and visited[j] == False:
                        queue.append(j)
                        visited[j] = True

    return answer
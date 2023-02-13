
from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    speeds = deque(speeds)
    
    while queue:
        tmp = 0
        for i in range(len(queue)):
            queue[i] += speeds[i] 
       
        while len(queue) > 0 and queue[0] >= 100:
            queue.popleft()
            speeds.popleft()
            tmp += 1

        if tmp != 0:
            answer.append(tmp)
        
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
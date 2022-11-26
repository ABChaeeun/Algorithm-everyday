from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    for _ in range(len(q1) * 3): # 최대 90만이라 시간초과x
        
        if sum1 == sum2:
            return answer
        
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())
            
        elif sum1 < sum2:
            sum1 += q2[0]
            sum2 -= q2[0]
            q1.append(q2.popleft())
                    
        answer += 1
        
    return -1

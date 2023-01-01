def solution(n):
    answer = 1 # 자기 자신
    
    lst = []
    for i in range(1, n//2+2):
        lst.append(i)
        
    for i in range(len(lst)):
        sum = 0
        for j in range(i, len(lst)):
            sum += lst[j]
            if sum == n:
                answer += 1
                break
            if sum > n:
                break
    
    if n == 1 or n == 2:
        answer = 1
        
    return answer

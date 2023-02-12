def solution(n):
    answer = 1
    tmp = 0
    
    for k in range(n//2 + 1, 0, -1):
        tmp = k
        for i in range(k-1, 0, -1):
            tmp += i
            if tmp > n:
                tmp = 0
                break
            elif tmp == n:
                answer += 1
                tmp = 0
                break
    
    return answer
    
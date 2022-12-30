def solution(num):
    answer = 0
    
    i = 0
    while(num != 1):
        
        if num % 2 == 0: # 짝수일 경우
            num = num // 2
        else: # 홀수일 경우
            num = num*3 + 1
        
        i += 1
        if i == 500: # 작업을 500번 반복할 때까지 1이 되지 않은 경우
            answer = -1
            break
        else:
            answer = i
            
    return answer

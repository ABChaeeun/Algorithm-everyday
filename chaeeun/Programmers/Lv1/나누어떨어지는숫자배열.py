def solution(arr, divisor):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            
    if answer:
        answer.sort()
    else:
        answer = [-1]
            
    return answer
# 결국 참고..
def GCD(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(arr):
    answer = arr[0]
    
    for num in arr:
        answer = answer*num // GCD(answer, num)
    
    return answer
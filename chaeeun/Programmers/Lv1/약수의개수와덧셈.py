def func(n):

    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    return len(lst)

def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        if func(num) % 2 == 0: # func() : 약수의 개수
            answer += num
        else:
            answer -= num
    
    return answer
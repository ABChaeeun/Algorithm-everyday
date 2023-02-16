def solution(s):
    answer = ''
    lst = list(s.split(' ')) # 하나 이상의 공백문자로 구분
    
    cnt = 0
    for word in lst:
        for i in range(len(word)):
            if i % 2 == 0: # 짝수
                answer += word[i].upper()
            elif i % 2 == 1: # 홀수
                answer += word[i].lower()
                
        cnt += 1
        if cnt != len(lst):
            answer += ' '
    
    return answer
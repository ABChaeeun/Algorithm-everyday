def solution(s):
    
    index = len(s) // 2
    
    if len(s) % 2 == 1:
        return s[index]
    else:
        return s[index-1:index+1]

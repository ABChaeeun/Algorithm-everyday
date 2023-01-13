def solution(s):
    answer = ''
    
    lst = []
    for i in range(len(s)):
        lst.append(ord(s[i]))
        
    lst.sort(reverse = True)
    
    for i in range(len(lst)):
        lst[i] = chr(lst[i])
        
    answer = ''.join(lst)
    return answer
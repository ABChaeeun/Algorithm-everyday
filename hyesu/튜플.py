def solution(s):
    answer = []
    s = s.replace('},', '} ').replace('{{', '{').replace('}}', '}')
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].replace('}','').replace('{', '')
        s[i] = list(map(int, s[i].split(',')))
    s.sort(key=len)
    
    for c in s:
        for k in c:
            if k not in answer:
                answer.append(k)
    
    return answer
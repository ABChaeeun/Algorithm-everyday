def solution(n, words):
    answer = [0, 0]
    
    lastChar = words[0][-1]
    index = 1

    for idx, word in enumerate(words):
        
        if idx == 0:
            continue
            
        if lastChar != word[0]:
            return [idx % n + 1, idx // n + 1]
        
        if words[:idx].count(word) >= 1:
            return [idx % n + 1, idx // n + 1]
            
        lastChar = word[len(word)-1]

    return answer
from collections import deque 

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    for city in cities:
        tmp = city.lower()
        if tmp in cache:
            answer += 1
            cache.remove(tmp)
            cache.append(tmp)
        else:
            answer += 5
            if len(cache) >= cacheSize:
                if cacheSize is not 0:
                    cache.popleft()
                    cache.append(tmp)
            else:
                cache.append(tmp)
    
    return answer
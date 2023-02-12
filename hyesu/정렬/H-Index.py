# 프로그래머스 Lv2 정렬 [H-Index]

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    max = citations[0]
    
    for i in range(max, -1, -1):
        if i <= len(list(filter(lambda x: x>=i, citations))):
            answer = i
            break

    return answer

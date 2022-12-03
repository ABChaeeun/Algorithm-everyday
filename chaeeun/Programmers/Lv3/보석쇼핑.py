def solution(gems):
    
    setlen = len(set(gems))

    dict = {gems[0]:1}
    lst = [0, len(gems)-1] # 가장 짧은 start, end 담을 리스트

    start = 0
    end = 0
    
    
    while start <= end and end < len(gems):

        # print(dict)
        
        if len(dict) == setlen: # gems의 모든 요소가 포함될 경우 (start +1)
            if end - start < lst[1] - lst[0]:
                # lst = [start+1, end+1] ### 여기서 해주면 안됨
                lst = [start, end]
            if dict[gems[start]] == 1:
                del dict[gems[start]]
            else:
                dict[gems[start]] -= 1
            start += 1

        else: # 아직 모든 요소가 포함되지 않는 경우 (end +1)
            end += 1
            if end >= len(gems): ## end의 범위 제한
                break
            if gems[end] not in dict:
                dict[gems[end]] = 1
            else:
                dict[gems[end]] += 1


    answer = [lst[0]+1, lst[1]+1]
    return answer


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))